# -*- encoding: utf-8 -*-
#
# (c) Copyright 2015 Hewlett Packard Enterprise Development LP
# Copyright 2015 Universidade Federal de Campina Grande
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

import json

import mock
import requests
import retrying
import six.moves.http_client as http_client
import unittest

from oneview_client import client
from oneview_client import exceptions
from oneview_client import states


PROPERTIES_DICT = {"cpu_arch": "x86_64",
                   "cpus": "8",
                   "local_gb": "10",
                   "memory_mb": "4096",
                   "capabilities": "server_hardware_type_uri:fake_sht_uri,"
                                   "enclosure_group_uri:fake_eg_uri"}

DRIVER_INFO_DICT = {'server_hardware_uri': 'fake_sh_uri',
                    'server_profile_template_uri': 'fake_spt_uri'}


class OneViewClientAuthTestCase(unittest.TestCase):

    def setUp(self):
        super(OneViewClientAuthTestCase, self).setUp()
        self.manager_url = 'https://1.2.3.4'
        self.username = 'user'
        self.password = 'password'

    @mock.patch.object(requests, 'post')
    def test_authenticate(self, mock_post):
        client.Client(self.manager_url,
                      self.username,
                      self.password)
        mock_post.assert_called_once_with(
            'https://1.2.3.4/rest/login-sessions',
            data=json.dumps({"userName": "user", "password": "password"}),
            headers={'content-type': 'application/json'},
            verify=True
        )

    @mock.patch.object(requests, 'post')
    def test_authenticate_insecure(self, mock_post):
        client.Client(self.manager_url,
                      self.username,
                      self.password,
                      allow_insecure_connections=True)
        mock_post.assert_called_once_with(
            'https://1.2.3.4/rest/login-sessions',
            data=json.dumps({"userName": "user", "password": "password"}),
            headers={'content-type': 'application/json'},
            verify=False
        )

    @mock.patch.object(requests, 'post')
    def test_authenticate_invalid_credentials(self, mock_post):
        response = mock_post.return_value
        response.status_code = http_client.BAD_REQUEST
        mock_post.return_value = response

        self.assertRaises(
            exceptions.OneViewNotAuthorizedException,
            client.Client,
            self.manager_url,
            'any',
            'any'
        )

    @mock.patch.object(client.Client, '_authenticate', autospec=True)
    def test_get_session(self, mock__authenticate):
        reference = "xyz"

        response = mock__authenticate.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(return_value={"sessionID": reference})
        mock__authenticate.return_value = response

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        session_id = oneview_client.get_session()
        self.assertEqual(reference, session_id)


@mock.patch.object(client.Client, '_authenticate', autospec=True)
class OneViewClientTestCase(unittest.TestCase):

    def setUp(self):
        super(OneViewClientTestCase, self).setUp()
        self.manager_url = 'https://1.2.3.4'
        self.username = 'user'
        self.password = 'password'

    @mock.patch.object(client.Client, 'set_node_power_state', autospec=True)
    @mock.patch.object(client.Client, 'get_node_power_state', autospec=True)
    def test_power_on_server_on(self, mock_get_pstate, mock_set_pstate,
                                mock__authenticate):
        driver_info = {"server_hardware_uri": "/any"}
        mock_get_pstate.return_value = states.ONEVIEW_POWER_ON
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        oneview_client.power_on(driver_info)
        mock_get_pstate.assert_called_once_with(oneview_client, driver_info)
        self.assertFalse(mock_set_pstate.called)

    @mock.patch.object(client.Client, 'set_node_power_state', autospec=True)
    @mock.patch.object(client.Client, 'get_node_power_state', autospec=True)
    def test_power_on_server_off(self, mock_get_pstate, mock_set_pstate,
                                 mock__authenticate):
        driver_info = {"server_hardware_uri": "/any"}
        mock_get_pstate.return_value = states.ONEVIEW_POWER_OFF
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        oneview_client.power_on(driver_info)
        mock_get_pstate.assert_called_once_with(oneview_client, driver_info)
        mock_set_pstate.assert_called_once_with(oneview_client, driver_info,
                                                states.ONEVIEW_POWER_ON)

    @mock.patch.object(client.Client, 'set_node_power_state', autospec=True)
    @mock.patch.object(client.Client, 'get_node_power_state', autospec=True)
    def test_power_off_server_off(self, mock_get_pstate, mock_set_pstate,
                                  mock__authenticate):
        driver_info = {"server_hardware_uri": "/any"}
        mock_get_pstate.return_value = states.ONEVIEW_POWER_OFF
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        oneview_client.power_off(driver_info)
        mock_get_pstate.assert_called_once_with(oneview_client, driver_info)
        self.assertFalse(mock_set_pstate.called)

    @mock.patch.object(client.Client, 'set_node_power_state', autospec=True)
    @mock.patch.object(client.Client, 'get_node_power_state', autospec=True)
    def test_power_off_server_on(self, mock_get_pstate, mock_set_pstate,
                                 mock__authenticate):
        driver_info = {"server_hardware_uri": "/any"}
        mock_get_pstate.return_value = states.ONEVIEW_POWER_ON
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        oneview_client.power_off(driver_info)
        mock_get_pstate.assert_called_once_with(oneview_client, driver_info)
        mock_set_pstate.assert_called_once_with(oneview_client, driver_info,
                                                states.ONEVIEW_POWER_OFF,
                                                client.PRESS_AND_HOLD)

    @mock.patch.object(client.Client, '_wait_for_task_to_complete',
                       autospec=True)
    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    @mock.patch.object(client.Client, 'get_node_power_state', autospec=True)
    def test_set_power_state_server_hardware(self, mock_get_node_power,
                                             mock__prepare_do_request,
                                             mock__wait_for_task,
                                             mock__authenticate):
        mock_get_node_power.return_value = states.ONEVIEW_POWER_ON
        mock__prepare_do_request.return_value = {}
        driver_info = {"server_hardware_uri": "/any"}

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        oneview_client.set_node_power_state(
            driver_info,
            states.ONEVIEW_POWER_ON
        )
        mock__prepare_do_request.assert_called_once_with(
            oneview_client,
            uri='/any/powerState',
            body={'powerControl': client.MOMENTARY_PRESS,
                  'powerState': states.ONEVIEW_POWER_ON},
            request_type=client.PUT_REQUEST_TYPE,
        )

    @mock.patch.object(requests, 'put', autospec=True)
    def test_set_power_state_nonexistent_server_hardware(
            self, mock_do_request, mock__authenticate):

        class Response(object):
            status_code = 404

            def json(self):
                return {
                    "errorCode": "RESOURCE_NOT_FOUND",
                    "details": "Resource not found, ID = /any_invalid",
                }

        mock_do_request.return_value = Response()

        driver_info = {"server_hardware_uri": "/any_invalid"}
        target_state = states.ONEVIEW_POWER_ON

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client.set_node_power_state, driver_info, target_state
        )

    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    @mock.patch.object(client.Client, 'get_node_power_state', autospec=True)
    def test_set_power_state_server_hardware_power_status_error(
        self, mock_get_node_power, mock__prepare_do_request, mock__authenticate
    ):
        power = states.ONEVIEW_ERROR
        mock_get_node_power.return_value = power
        mock__prepare_do_request.return_value = {
            "taskState": "Error",
            "percentComplete": 100
        }
        driver_info = {"server_hardware_uri": "/any"}
        target_state = "On"

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        self.assertRaises(
            exceptions.OneViewErrorStateSettingPowerState,
            oneview_client.set_node_power_state, driver_info, target_state
        )

    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    def test_get_server_hardware_nonexistent(self, mock__prepare_do_request,
                                             mock__authenticate):
        mock__prepare_do_request.return_value = {"error": "resource not found"}
        driver_info = {"server_hardware_uri": ""}

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client.get_server_hardware,
            driver_info
        )

    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    @mock.patch.object(client.Client, 'get_server_profile_from_hardware',
                       autospec=True)
    def test_set_boot_device_nonexistent_resource_uri(self,
                                                      mock_get_server_profile,
                                                      mock__prepare_do_request,
                                                      mock__authenticate):
        driver_info = {}
        new_first_boot_device = "None"
        mock__prepare_do_request.return_value = {
            "errorCode": "RESOURCE_NOT_FOUND",
            "data": None
        }

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client.set_boot_device,
            driver_info,
            new_first_boot_device
        )

    @mock.patch.object(client.Client, 'get_boot_order', autospec=True)
    def test_set_boot_device_nonexistent_resource_first_boot_device(
        self, mock_get_boot_order, mock__authenticate
    ):
        driver_info = {}
        new_first_boot_device = None
        mock_get_boot_order.return_value = []

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        self.assertRaises(
            exceptions.OneViewBootDeviceInvalidError,
            oneview_client.set_boot_device,
            driver_info,
            new_first_boot_device
        )

    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    @mock.patch.object(client.Client, 'get_boot_order', autospec=True)
    def test_get_server_profile_from_hardware(self, mock_get_boot_order,
                                              mock_get_server_hardware,
                                              mock__prepare_do_request,
                                              mock__authenticate):
        driver_info = {}
        new_first_boot_device = "any_boot_device"
        mock_get_boot_order.return_value = []
        mock_get_server_hardware.return_value = {}

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        self.assertRaises(
            exceptions.OneViewServerProfileAssociatedError,
            oneview_client.set_boot_device,
            driver_info,
            new_first_boot_device
        )

        mock_get_server_hardware.return_value = {"serverProfileUri": "any_uri"}
        mock__prepare_do_request.return_value = {}

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client.set_boot_device,
            driver_info,
            new_first_boot_device
        )

    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    def test__wait_for_task_to_complete(self, mock__prepare_do_request,
                                        mock__authenticate):
        task = {
            "uri": "/any_uri",
            "taskState": "Something",
            "percentComplete": 100
        }

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password,
                                       max_polling_attempts=1)

        mock__prepare_do_request.return_value = task
        oneview_client._wait_for_task_to_complete(task)

    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    def test__wait_for_task_to_complete_timeout(self, mock__prepare_do_request,
                                                mock__authenticate):
        task = {
            "uri": "/any_uri",
            "taskState": "Something",
            "percentComplete": 30
        }

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password,
                                       max_polling_attempts=1)

        mock__prepare_do_request.return_value = task
        self.assertRaises(
            retrying.RetryError,
            oneview_client._wait_for_task_to_complete,
            task,
        )

    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    def test_validate_node_server_hardware_inconsistent_memorymb_value(
        self, mock_get_server_hardware, mock__authenticate
    ):
        mock_get_server_hardware.return_value = {
            "memoryMb": 1,
            "processorCoreCount": 1,
            "processorCount": 1,
        }
        driver_info = {
            "server_hardware_uri": "/any_uri",
        }
        node_memorymb = 2
        node_cpus = 1

        exc_expected_msg = (
            "Node memory_mb is inconsistent with OneView's server"
            " hardware /any_uri memoryMb."
        )

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            oneview_client.validate_node_server_hardware,
            driver_info,
            node_memorymb,
            node_cpus
        )

    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    def test_validate_node_server_hardware_inconsistent_cpus_value(
        self, mock_get_server_hardware, mock__authenticate
    ):
        mock_get_server_hardware.return_value = {
            "memoryMb": 1,
            "processorCoreCount": 2,
            "processorCount": 3,
        }
        driver_info = {
            "server_hardware_uri": "/any_uri",
        }
        node_memorymb = 1
        node_cpus = 3

        exc_expected_msg = (
            "Node cpus is inconsistent with OneView's server"
            " hardware /any_uri cpus."
        )

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            oneview_client.validate_node_server_hardware,
            driver_info,
            node_memorymb,
            node_cpus
        )

    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    def test_validate_node_server_hardware_type_inconsistent_sht_uri(
        self, mock_get_server_hardware, mock__authenticate
    ):
        mock_get_server_hardware.return_value = {
            "serverHardwareTypeUri": "/incosistent_uri"
        }
        driver_info = {
            "server_hardware_uri": "/any_serveruri",
            "server_hardware_type_uri": "/any_uri",
        }

        exc_expected_msg = (
            "Node server_hardware_type_uri is inconsistent with"
            " OneView's server hardware /any_serveruri serverHardwareTypeUri."
        )

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            oneview_client.validate_node_server_hardware_type,
            driver_info
        )

    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    def test_validate_node_enclosure_group_inconsistent(
        self, mock_get_server_hardware, mock__authenticate
    ):
        driver_info = {
            "server_hardware_uri": "/any_uri",
            "enclosure_group_uri": "/inconsistent_uri"
        }

        exc_expected_msg = (
            "Node enclosure_group_uri is inconsistent with"
            " OneView's server hardware /any_uri serverGroupUri."
        )

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            oneview_client.validate_node_enclosure_group,
            driver_info
        )

    @mock.patch.object(client.Client, 'get_server_profile_from_hardware',
                       autospec=True)
    def test_check_node_port_mac_incompatible_with_server_profile(
        self, mock_server_profile, mock__authenticate
    ):
        mock_server_profile.return_value = {
            "uri": "/anyuri",
            "connections": [
                {'boot': {'priority': u'Primary'},
                 'mac': u'56:88:7B:C0:00:0B'}
            ]
        }

        exc_expected_msg = (
            "The ports of the node are not compatible with its"
            " server profile /anyuri."
        )

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            oneview_client
            .is_node_port_mac_compatible_with_server_profile,
            {},
            {}
        )

    @mock.patch.object(client.Client, 'get_server_profile_from_hardware',
                       autospec=True)
    def test_check_node_port_mac_no_primary_boot_connection(
        self, mock_server_profile, mock__authenticate
    ):
        mock_server_profile.return_value = {
            "uri": "/anyuri",
            "connections": [
                {'boot': {'priority': u'NotBootable'},
                 'mac': u'56:88:7B:C0:00:0B'}
            ]
        }

        exc_expected_msg = (
            "No primary boot connection configured for server profile"
            " /anyuri."
        )

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            oneview_client
            .is_node_port_mac_compatible_with_server_profile,
            {},
            {}
        )

    @mock.patch.object(client.Client, 'get_server_profile_template',
                       autospec=True)
    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    def test_validate_node_server_profile_template_inconsistent_sht(
        self, mock_server_hardware, mock_server_template, mock__authenticate
    ):
        mock_server_hardware.return_value = {
            'serverHardwareTypeUri': '/sht_uri',
            'serverGroupUri': 'eg_uri'}
        mock_server_template.return_value = {
            'serverHardwareTypeUri': '/inconsistent_uri',
            'enclosureGroupUri': '/inconsistent_uri'}

        driver_info = {
            "server_hardware_uri": "/any_uri",
            "server_profile_template_uri": "/profile_uri"
        }

        exc_expected_msg = (
            "Server profile template /profile_uri serverHardwareTypeUri is"
            " inconsistent with server hardware /any_uri"
            " serverHardwareTypeUri."
        )

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            oneview_client.validate_node_server_profile_template,
            driver_info
        )

    @mock.patch.object(client.Client, 'get_server_profile_template',
                       autospec=True)
    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    def test_validate_node_server_profile_template_inconsistent_eg(
        self, mock_server_hardware, mock_server_template, mock__authenticate
    ):
        mock_server_hardware.return_value = {
            'serverHardwareTypeUri': '/sht_uri',
            'serverGroupUri': 'eg_uri'}
        mock_server_template.return_value = {
            'serverHardwareTypeUri': '/sht_uri',
            'enclosureGroupUri': '/inconsistent_uri'}

        driver_info = {
            "server_hardware_uri": "/any_uri",
            "server_profile_template_uri": "/profile_uri"
        }

        exc_expected_msg = (
            "Server profile template /profile_uri enclosureGroupUri is"
            " inconsistent with server hardware /any_uri"
            " serverGroupUri."
        )

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            oneview_client.validate_node_server_profile_template,
            driver_info
        )

    @mock.patch.object(client.Client, 'get_oneview_version')
    def test_verify_oneview_version(self, mock_get_oneview_version,
                                    mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        mock_get_oneview_version.return_value = {
            'minimumVersion': 120,
            'currentVersion': 200
        }
        oneview_client.verify_oneview_version()
        mock_get_oneview_version.assert_called_once_with()

    @mock.patch.object(client.Client, 'get_oneview_version')
    def test_verify_oneview_version_fail(self, mock_get_oneview_version,
                                         mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        mock_get_oneview_version.return_value = {
            'minimumVersion': 120,
            'currentVersion': 120
        }
        self.assertRaises(
            exceptions.IncompatibleOneViewAPIVersion,
            oneview_client.verify_oneview_version
        )
