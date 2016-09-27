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

import copy
import json

import mock
import requests
import retrying
import six.moves.http_client as http_client
import unittest

from oneview_client import client
from oneview_client import exceptions
from oneview_client import models
from oneview_client import states
from oneview_client.tests import fixtures


class TestablePort(object):

    def __init__(self, obj_address):
        self.obj_address = obj_address
        self._obj_address = obj_address


class OneViewClientAuthTestCase(unittest.TestCase):

    @mock.patch.object(client.Client, '_authenticate', autospec=True)
    def setUp(self, mock__authenticate):
        super(OneViewClientAuthTestCase, self).setUp()
        self.manager_url = 'https://1.2.3.4'
        self.username = 'user'
        self.password = 'password'
        self.oneview_client = client.Client(
            self.manager_url,
            self.username,
            self.password
        )

    @mock.patch.object(requests, 'post')
    def test_authenticate(self, mock_post):
        client.Client(
            self.manager_url,
            self.username,
            self.password
        )
        mock_post.assert_called_once_with(
            'https://1.2.3.4/rest/login-sessions',
            data=json.dumps({"userName": "user", "password": "password"}),
            headers={'content-type': 'application/json'},
            verify=True
        )

    @mock.patch.object(requests, 'post')
    def test_authenticate_insecure(self, mock_post):
        client.Client(
            self.manager_url,
            self.username,
            self.password,
            allow_insecure_connections=True
        )
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
        reference = "XYZ"
        response = mock__authenticate.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(return_value={'sessionID': reference})
        mock__authenticate.return_value = response
        oneview_client = client.Client(
            self.manager_url,
            self.username,
            self.password
        )
        oneview_client._authenticate = mock__authenticate
        self.assertEqual("XYZ", self.oneview_client.get_session())

    @mock.patch.object(client.Client, '_authenticate', autospec=True)
    @mock.patch.object(requests, 'delete', autospec=True)
    def test__logout(self,
                     mock_delete,
                     mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        oneview_client._logout()
        mock_delete.assert_called_once_with(
            url='https://1.2.3.4/rest/login-sessions',
            headers=mock.ANY,
            verify=True
        )


class OneViewClientTestCase(unittest.TestCase):

    @mock.patch.object(client.Client, '_authenticate', autospec=True)
    def setUp(self, mock__authenticate):
        super(OneViewClientTestCase, self).setUp()
        self.manager_url = 'https://1.2.3.4'
        self.username = 'user'
        self.password = 'password'
        self.oneview_client = client.Client(
            self.manager_url, self.username, self.password
        )

    @mock.patch.object(client.Client, 'set_node_power_state', autospec=True)
    @mock.patch.object(client.Client, 'get_node_power_state', autospec=True)
    def test_power_on_server_on(self, mock_get_pstate, mock_set_pstate):
        driver_info = {"server_hardware_uri": "/any"}
        mock_get_pstate.return_value = states.ONEVIEW_POWER_ON
        self.oneview_client.power_on(driver_info)
        mock_get_pstate.assert_called_once_with(
            self.oneview_client, driver_info
        )
        self.assertFalse(mock_set_pstate.called)

    @mock.patch.object(client.Client, 'set_node_power_state', autospec=True)
    @mock.patch.object(client.Client, 'get_node_power_state', autospec=True)
    def test_power_on_server_off(
        self, mock_get_pstate, mock_set_pstate
    ):
        driver_info = {"server_hardware_uri": "/any"}
        mock_get_pstate.return_value = states.ONEVIEW_POWER_OFF
        self.oneview_client.power_on(driver_info)
        mock_get_pstate.assert_called_once_with(
            self.oneview_client,
            driver_info
        )
        mock_set_pstate.assert_called_once_with(
            self.oneview_client,
            driver_info,
            states.ONEVIEW_POWER_ON
        )

    @mock.patch.object(client.Client, 'set_node_power_state', autospec=True)
    @mock.patch.object(client.Client, 'get_node_power_state', autospec=True)
    def test_power_off_server_off(self, mock_get_pstate, mock_set_pstate):
        driver_info = {"server_hardware_uri": "/any"}
        mock_get_pstate.return_value = states.ONEVIEW_POWER_OFF
        self.oneview_client.power_off(driver_info)
        mock_get_pstate.assert_called_once_with(
            self.oneview_client, driver_info
        )
        self.assertFalse(mock_set_pstate.called)

    @mock.patch.object(client.Client, 'set_node_power_state', autospec=True)
    @mock.patch.object(client.Client, 'get_node_power_state', autospec=True)
    def test_power_off_server_on(
        self, mock_get_pstate, mock_set_pstate
    ):
        driver_info = {"server_hardware_uri": "/any"}
        mock_get_pstate.return_value = states.ONEVIEW_POWER_ON
        self.oneview_client.power_off(driver_info)
        mock_get_pstate.assert_called_once_with(
            self.oneview_client,
            driver_info
        )
        mock_set_pstate.assert_called_once_with(
            self.oneview_client,
            driver_info,
            states.ONEVIEW_POWER_OFF,
            client.PRESS_AND_HOLD
        )

    @mock.patch.object(client.Client, '_wait_for_task_to_complete',
                       autospec=True)
    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    @mock.patch.object(client.Client, 'get_node_power_state', autospec=True)
    def test_set_power_state_server_hardware(
        self, mock_get_node_power, mock__prepare_do_request,
        mock__wait_for_task
    ):
        mock_get_node_power.return_value = states.ONEVIEW_POWER_ON
        mock__prepare_do_request.return_value = {}
        driver_info = {"server_hardware_uri": "/any"}

        self.oneview_client.set_node_power_state(
            driver_info,
            states.ONEVIEW_POWER_ON
        )
        mock__prepare_do_request.assert_called_once_with(
            self.oneview_client,
            uri='/any/powerState',
            body={'powerControl': client.MOMENTARY_PRESS,
                  'powerState': states.ONEVIEW_POWER_ON},
            request_type=client.PUT_REQUEST_TYPE,
        )

    @mock.patch.object(requests, 'put', autospec=True)
    def test_set_power_state_nonexistent_server_hardware(
        self, mock_do_request
    ):
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

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            self.oneview_client.set_node_power_state, driver_info, target_state
        )

    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    @mock.patch.object(client.Client, 'get_node_power_state', autospec=True)
    def test_set_power_state_server_hardware_power_status_unknown(
        self, mock_get_node_power, mock__prepare_do_request
    ):
        power = states.ONEVIEW_UNKNOWN
        mock_get_node_power.return_value = power
        mock__prepare_do_request.return_value = {
            "taskState": "Error",
            "percentComplete": 100
        }
        driver_info = {"server_hardware_uri": "/any"}
        target_state = "On"

        self.assertRaises(
            exceptions.OneViewErrorStateSettingPowerState,
            self.oneview_client.set_node_power_state, driver_info, target_state
        )

    @mock.patch.object(requests, 'get')
    def test_get_server_hardware_nonexistent(self, mock_get):
        response = mock_get.return_value
        response.status_code = http_client.NOT_FOUND
        mock_get.return_value = response
        driver_info = {"server_hardware_uri": ""}

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            self.oneview_client.get_server_hardware,
            driver_info
        )

    @mock.patch.object(requests, 'get')
    def test_get_server_hardware_nonexistent_by_uuid(self, mock_get):
        response = mock_get.return_value
        response.status_code = http_client.NOT_FOUND
        mock_get.return_value = response
        uuid = 0
        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            self.oneview_client.get_server_hardware_by_uuid,
            uuid
        )

    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    def test_get_server_hardware_by_uuid(self, mock__prepare_do_request):
        mock__prepare_do_request.return_value = {
            "uri": "/rest/server-hardware/555",
            "processorCoreCount": 5,
            "processorCount": 2,
        }
        uuid = 555
        sh = self.oneview_client.get_server_hardware_by_uuid(uuid)
        self.assertEqual(sh.cpus, 10)
        mock__prepare_do_request.assert_called_once_with(
            self.oneview_client, uri="/rest/server-hardware/555"
        )

    @mock.patch.object(client.Client, '_set_onetime_boot')
    @mock.patch.object(client.Client, '_wait_for_task_to_complete',
                       autospec=True)
    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    @mock.patch.object(client.Client, 'get_server_profile_from_hardware',
                       autospec=True)
    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    def test_set_boot_device(
        self, mock_get_server_hardware, mock_get_server_profile,
        mock__prepare_do_request, mock__wait_for_task, mock_set_onetime_boot
    ):

        server_hardware = (
            models.ServerHardware.from_json(fixtures.SERVER_HARDWARE_JSON)
        )
        mock_get_server_hardware.return_value = server_hardware
        profile = copy.deepcopy(fixtures.SERVER_PROFILE_JSON)
        mock_get_server_profile.return_value = (
            models.ServerProfile.from_json(profile)
        )
        expected_profile = copy.deepcopy(fixtures.SERVER_PROFILE_JSON)
        expected_profile['boot'] = {
            'manageBoot': True,
            # Original boot order is ["CD", "Floppy", "USB", "HardDisk", "PXE"]
            'order': ["PXE", "CD", "Floppy", "USB", "HardDisk"]
        }
        driver_info = {"server_hardware_uri": "/any"}
        new_first_boot_device = "PXE"
        # Persistent
        self.oneview_client.set_boot_device(driver_info, new_first_boot_device)
        mock__prepare_do_request.assert_called_once_with(
            self.oneview_client,
            body=expected_profile,
            request_type='PUT',
            uri='/rest/server-profiles/f2160e28-8107-45f9-b4b2-3119a622a3a1'
        )
        # Onetime
        new_first_boot_device = "USB"
        self.oneview_client.set_boot_device(driver_info, new_first_boot_device,
                                            onetime=True)
        mock_set_onetime_boot.assert_called_once_with(
            'any',
            new_first_boot_device
        )
        # Fallback in case onetime fails
        new_first_boot_device = "HardDisk"
        mock__prepare_do_request.reset_mock()
        mock_set_onetime_boot.reset_mock()
        expected_profile['boot'] = {
            'manageBoot': True,
            # Boot order should be ["PXE", "CD", "Floppy", "USB", "HardDisk"]
            'order': ["HardDisk", "PXE", "CD", "Floppy", "USB"]
        }
        mock_set_onetime_boot.side_effect = [exceptions.IloException("BOOM")]
        self.oneview_client.set_boot_device(driver_info, new_first_boot_device,
                                            onetime=True)
        mock__prepare_do_request.assert_called_once_with(
            self.oneview_client,
            body=expected_profile,
            request_type='PUT',
            uri='/rest/server-profiles/f2160e28-8107-45f9-b4b2-3119a622a3a1'
        )

    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    @mock.patch.object(client.Client, 'get_server_profile_from_hardware',
                       autospec=True)
    def test_set_boot_device_nonexistent_resource_uri(
        self, mock_get_server_profile, mock__prepare_do_request
    ):
        driver_info = {}
        new_first_boot_device = "None"
        mock__prepare_do_request.return_value = {
            "errorCode": "RESOURCE_NOT_FOUND",
            "data": None
        }

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            self.oneview_client.set_boot_device,
            driver_info,
            new_first_boot_device
        )

    @mock.patch.object(client.Client, 'get_boot_order', autospec=True)
    def test_set_boot_device_nonexistent_resource_first_boot_device(
        self, mock_get_boot_order
    ):
        driver_info = {}
        new_first_boot_device = None
        mock_get_boot_order.return_value = []

        self.assertRaises(
            exceptions.OneViewBootDeviceInvalidError,
            self.oneview_client.set_boot_device,
            driver_info,
            new_first_boot_device
        )

    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    def test_get_server_profile_from_hardware(
        self, mock_get_server_hardware, mock__prepare_do_request
    ):
        driver_info = {}
        server_hardware = models.ServerHardware()
        setattr(server_hardware, 'server_profile_uri', None)
        mock_get_server_hardware.return_value = server_hardware

        self.assertRaises(
            exceptions.OneViewServerProfileAssociatedError,
            self.oneview_client.get_server_profile_from_hardware,
            driver_info
        )
        setattr(
            server_hardware,
            'server_profile_uri',
            'any_uri'
        )
        mock_get_server_hardware.return_value = server_hardware
        mock__prepare_do_request.return_value = {}

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            self.oneview_client.get_server_profile_from_hardware,
            driver_info
        )

    @mock.patch.object(requests, 'get')
    def test_get_server_profile_template_nonexistent_by_uuid(self, mock_get):
        response = mock_get.return_value
        response.status_code = http_client.NOT_FOUND
        mock_get.return_value = response
        uuid = 0
        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            self.oneview_client.get_server_profile_template_by_uuid,
            uuid
        )

    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    def test_get_server_profile_template_by_uuid(
        self, mock__prepare_do_request
    ):
        mock__prepare_do_request.return_value = {
            "uri": "/rest/server-profile-templates/123"
        }
        uuid = 123
        self.oneview_client.get_server_profile_template_by_uuid(uuid)
        mock__prepare_do_request.assert_called_once_with(
            self.oneview_client, uri="/rest/server-profile-templates/123"
        )

    @mock.patch.object(requests, 'get')
    def test_get_server_profile_nonexistent_by_uuid(
        self, mock_get
    ):
        response = mock_get.return_value
        response.status_code = http_client.NOT_FOUND
        mock_get.return_value = response
        uuid = 0
        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            self.oneview_client.get_server_profile_by_uuid,
            uuid
        )

    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    def test_get_server_profile_by_uuid(
        self, mock__prepare_do_request
    ):
        server_profile_uuid = 123
        server_profile_uri = "/rest/server-profiles/" + \
            str(server_profile_uuid)
        mock__prepare_do_request.return_value = {
            "uri": server_profile_uri
        }
        self.oneview_client.get_server_profile_by_uuid(server_profile_uuid)
        mock__prepare_do_request.assert_called_once_with(
            self.oneview_client, uri=server_profile_uri
        )

    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    def test__wait_for_task_to_complete(self, mock__prepare_do_request):

        task0 = {
            "uri": "/any_uri",
            "taskState": "Something",
            "percentComplete": 0
        }

        task1 = {
            "uri": "/any_uri",
            "taskState": "Something",
            "percentComplete": 10
        }

        task2 = {
            "uri": "/any_uri",
            "taskState": "Something",
            "percentComplete": 50
        }

        task3 = {
            "uri": "/any_uri",
            "taskState": "Something",
            "percentComplete": 100
        }

        mock__prepare_do_request.side_effect = [task1, task2, task3]
        self.oneview_client._wait_for_task_to_complete(task0)

    @mock.patch.object(client.Client, '_authenticate', autospec=True)
    @mock.patch.object(requests, 'get')
    def test__wait_for_task_to_complete_timeout(
        self, mock_get, mock__authenticate
    ):
        task = {
            "uri": "/any_uri",
            "taskState": "Something",
            "percentComplete": 0
        }

        oneview_client = client.Client(
            self.manager_url,
            self.username,
            self.password,
            max_polling_attempts=2
        )

        response = mock_get.return_value
        response.status_code = http_client.REQUEST_TIMEOUT
        mock_get.return_value = response

        self.assertRaises(
            retrying.RetryError,
            oneview_client._wait_for_task_to_complete,
            task,
        )
        self.assertEqual(mock_get.call_count, 2)

    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    def test_validate_node_server_hardware_inconsistent_memorymb_value(
        self, mock_get_server_hardware
    ):
        server_hardware_mock = models.ServerHardware()
        setattr(server_hardware_mock, "processor_core_count", 1)
        setattr(server_hardware_mock, "processor_count", 1)
        setattr(server_hardware_mock, "memory_mb", 1)

        mock_get_server_hardware.return_value = server_hardware_mock

        driver_info = {
            "server_hardware_uri": "/any_uri",
        }
        node_memorymb = 2
        node_cpus = 1

        exc_expected_msg = (
            "Node memory_mb is inconsistent with OneView's server"
            " hardware /any_uri memoryMb."
        )

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            self.oneview_client.validate_node_server_hardware,
            driver_info,
            node_memorymb,
            node_cpus
        )

    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    def test_validate_node_server_hardware_type_inconsistent_sht_uri(
        self, mock_get_server_hardware
    ):
        server_hardware_mock = models.ServerHardware()
        setattr(server_hardware_mock,
                "server_hardware_type_uri",
                "/incosistent_uri")

        mock_get_server_hardware.return_value = server_hardware_mock

        driver_info = {
            "server_hardware_uri": "/any_serveruri",
            "server_hardware_type_uri": "/any_uri",
        }

        exc_expected_msg = (
            "Node server_hardware_type_uri is inconsistent with"
            " OneView's server hardware /any_serveruri serverHardwareTypeUri."
        )

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            self.oneview_client.validate_node_server_hardware_type,
            driver_info
        )

    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    def test_validate_node_enclosure_group_inconsistent(
        self, mock_get_server_hardware
    ):
        server_hardware = models.ServerHardware()
        server_hardware.uuid = "aaaa-bbbb-cccc"
        server_hardware.enclosure_group_uri = "/my-real-enclosure-group"
        mock_get_server_hardware.return_value = server_hardware
        driver_info = {
            "server_hardware_uri": "/any_uri",
            "enclosure_group_uri": "/inconsistent_uri"
        }

        exc_expected_msg = (
            "Node enclosure_group_uri '/inconsistent_uri' is inconsistent "
            "with OneView's server hardware serverGroupUri "
            "'/my-real-enclosure-group' of ServerHardware aaaa-bbbb-cccc"
        )

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            self.oneview_client.validate_node_enclosure_group,
            driver_info
        )

    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    def test_validate_node_server_hardware_values_as_string(
        self, mock_get_server_hardware
    ):
        server_hardware_mock = models.ServerHardware()
        setattr(server_hardware_mock, "processor_core_count", 2)
        setattr(server_hardware_mock, "processor_count", 3)
        setattr(server_hardware_mock, "memory_mb", 1)

        mock_get_server_hardware.return_value = server_hardware_mock

        driver_info = {
            "server_hardware_uri": "/any_uri",
            "enclosure_group_uri": "/inconsistent_uri"
        }
        node_memorymb = '1'
        node_cpus = '6'

        self.assertIsNone(
            self.oneview_client.validate_node_server_hardware(
                driver_info, node_memorymb, node_cpus)
        )

    @mock.patch.object(client.Client, 'get_server_hardware_by_uuid',
                       autospec=True)
    @mock.patch.object(client.Client, 'get_server_hardware',
                       autospec=True)
    def test_is_node_port_mac_compatible_with_server_hardware(
        self, mock_server_hardware, mock_server_hardware_by_uuid,
    ):
        server_hardware_mock = models.ServerHardware()
        setattr(server_hardware_mock, "uri", "/anyuri")
        setattr(server_hardware_mock, "uuid", "1111-2222-3333")
        server_hardware_mock_port_map = fixtures.PORT_MAP
        setattr(server_hardware_mock,
                "port_map",
                server_hardware_mock_port_map)

        mock_server_hardware.return_value = server_hardware_mock
        mock_server_hardware_by_uuid.return_value = server_hardware_mock

        self.oneview_client.is_node_port_mac_compatible_with_server_hardware(
            {},
            [type('obj', (object,), {'_address': 'D8:9D:67:73:54:00'})]
        )

        mock_server_hardware.assert_called_once_with(self.oneview_client, {})

    @mock.patch.object(client.Client, 'get_server_hardware_by_uuid',
                       autospec=True)
    @mock.patch.object(client.Client, 'get_server_hardware',
                       autospec=True)
    def test_is_node_port_mac_incompatible_with_server_hardware(
        self, mock_server_hardware, mock_server_hardware_by_uuid,
    ):
        server_hardware_mock = models.ServerHardware()
        setattr(server_hardware_mock, "uri", "/anyuri")
        setattr(server_hardware_mock, "uuid", "1111-2222-3333")
        server_hardware_mock_port_map = fixtures.PORT_MAP
        setattr(server_hardware_mock,
                "port_map",
                server_hardware_mock_port_map)

        mock_server_hardware.return_value = server_hardware_mock
        mock_server_hardware_by_uuid.return_value = server_hardware_mock

        exc_expected_msg = (
            "The ports of the node are not compatible with its server hardware"
            " /anyuri."
        )

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            self.oneview_client
            .is_node_port_mac_compatible_with_server_hardware,
            {},
            [type('obj', (object,), {'_address': 'AA:BB:CC:DD:EE:FF'})]
        )

    @mock.patch.object(client.Client, 'get_server_profile_from_hardware',
                       autospec=True)
    def test_check_node_port_mac_incompatible_with_server_profile(
        self, mock_server_profile
    ):
        server_profile_mock = models.ServerProfile()
        setattr(server_profile_mock, "uri", "/anyuri")
        server_profile_mock_connections = [
            {'boot': {'priority': u'Primary'},
             'mac': u'56:88:7B:C0:00:0B'}
        ]
        setattr(server_profile_mock,
                "connections",
                server_profile_mock_connections)

        mock_server_profile.return_value = server_profile_mock

        exc_expected_msg = (
            "The ports of the node are not compatible with its"
            " server profile /anyuri."
        )

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            self.oneview_client
            .is_node_port_mac_compatible_with_server_profile,
            {},
            {}
        )

    @mock.patch.object(client.Client, 'get_server_profile_from_hardware',
                       autospec=True)
    def test_check_node_port_server_profile_mac_no_primary_boot_connection(
        self, mock_server_profile
    ):
        server_profile_mock = models.ServerProfile()
        setattr(server_profile_mock, "uri", "/anyuri")
        server_profile_mock_connections = [
            {'boot': {'priority': u'NotBootable'},
             'mac': u'56:88:7B:C0:00:0B'}
        ]
        setattr(server_profile_mock,
                "connections",
                server_profile_mock_connections)

        mock_server_profile.return_value = server_profile_mock

        exc_expected_msg = (
            "No primary boot connection configured for server profile"
            " /anyuri."
        )

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            self.oneview_client
            .is_node_port_mac_compatible_with_server_profile,
            {},
            {}
        )

    def test_validate_node_server_profile_template_inconsistent_sht(self):
        server_profile_template = models.ServerProfileTemplate()
        setattr(server_profile_template, "uri", "/any_uri")
        setattr(
            server_profile_template, "server_hardware_type_uri", "/any_uri"
        )

        server_hardware = models.ServerHardware()
        setattr(server_hardware, "uri", "/any_uri")
        setattr(server_hardware, "server_hardware_type_uri", "/sht_uri")

        with self.assertRaises(exceptions.OneViewInconsistentResource):
            self.oneview_client._validate_spt_server_hardware_type(
                server_profile_template, server_hardware
            )

    def test_validate_node_server_profile_template_inconsistent_eg(self):
        server_profile_template = models.ServerProfileTemplate()
        setattr(server_profile_template, "uri", "/any_uri")
        setattr(server_profile_template, "enclosure_group_uri", "/any_uri")

        server_hardware = models.ServerHardware()
        setattr(server_hardware, "uri", "/any_uri")
        setattr(server_hardware, "enclosure_group_uri", "/eg_uri")

        with self.assertRaises(exceptions.OneViewInconsistentResource):
            self.oneview_client._validate_spt_enclosure_group(
                server_profile_template, server_hardware
            )

    def test__validate_server_profile_template_manage_boot(self):
        server_profile_template = models.ServerProfileTemplate()
        setattr(server_profile_template, "uri", "/any_uri")
        spt_manage_boot = {'manageBoot': True}
        setattr(server_profile_template, "boot", spt_manage_boot)

        self.oneview_client._validate_spt_manage_boot(
            server_profile_template
        )

    def test__validate_server_profile_template_manage_boot_false(self):
        server_profile_template = models.ServerProfileTemplate()
        setattr(server_profile_template, "uri", "/any_uri")
        spt_manage_boot = {'manageBoot': False}
        setattr(server_profile_template, "boot", spt_manage_boot)

        with self.assertRaises(exceptions.OneViewInconsistentResource):
            self.oneview_client._validate_spt_manage_boot(
                server_profile_template
            )

    def test__validate_spt_boot_connections(self):
        server_profile_template = models.ServerProfileTemplate()
        setattr(server_profile_template, "uri", "/template_uri")
        profile_template_mock_connections = [
            {'boot': {'priority': u'Primary'},
             'mac': u'56:88:7B:C0:00:0B'}
        ]
        setattr(server_profile_template,
                "connections",
                profile_template_mock_connections)

        self.oneview_client._validate_spt_boot_connections(
            server_profile_template
        )

    def test__validate_spt_boot_connections_no_primary_boot(self):
        server_profile_template = models.ServerProfileTemplate()
        setattr(server_profile_template, "uri", "/template_uri")

        profile_template_mock_connections = [
            {'boot': {'priority': u'NotBootable'},
             'mac': u'56:88:7B:C0:00:0B'}
        ]
        setattr(server_profile_template,
                "connections",
                profile_template_mock_connections)

        with self.assertRaises(exceptions.OneViewInconsistentResource):
            self.oneview_client._validate_spt_boot_connections(
                server_profile_template
            )

    def test__validate_spt_boot_connections_more_than_one_connection(self):
        server_profile_template = models.ServerProfileTemplate()
        setattr(server_profile_template, "uri", "/template_uri")

        # More than one connection, Primary first
        profile_template_mock_connections = [
            {'boot': {'priority': u'Primary'},
             'mac': u'56:88:7B:C0:00:0B'},
            {'boot': {'priority': u'NotBootable'},
             'mac': u'56:88:7B:C0:00:0C'}
        ]
        setattr(server_profile_template,
                "connections",
                profile_template_mock_connections)

        self.oneview_client._validate_spt_boot_connections(
            server_profile_template
        )

        # More than one connection, Primary NOT first
        profile_template_mock_connections = [
            {'boot': {'priority': u'NotBootable'},
             'mac': u'56:88:7B:C0:00:0B'},
            {'boot': {'priority': u'Primary'},
             'mac': u'56:88:7B:C0:00:0C'}
        ]
        setattr(server_profile_template,
                "connections",
                profile_template_mock_connections)

        self.oneview_client._validate_spt_boot_connections(
            server_profile_template
        )

    @mock.patch.object(client.Client, 'get_server_profile_template_by_uuid',
                       autospec=True)
    def test_validate_server_profile_template_mac_type(
            self, server_template_mock):
        uuid = 123

        profile_template_mock = models.ServerProfileTemplate()
        setattr(profile_template_mock, "mac_type", "Physical")

        server_template_mock.return_value = profile_template_mock
        self.oneview_client.validate_server_profile_template_mac_type(uuid)

    @mock.patch.object(client.Client, 'get_server_profile_template_by_uuid',
                       autospec=True)
    def test_validate_server_profile_template_mac_type_negative(
            self, server_template_mock):
        uuid = 123

        # Negative case
        profile_template_mock = models.ServerProfileTemplate()
        setattr(profile_template_mock, "mac_type", "Virtual")
        setattr(profile_template_mock, "uri",
                "/rest/server-profile-templates/%s" % uuid)

        server_template_mock.return_value = profile_template_mock
        self.assertRaises(
            exceptions.OneViewInconsistentResource,
            self.oneview_client.validate_server_profile_template_mac_type,
            uuid)

    @mock.patch.object(client.Client, 'get_oneview_version')
    def test_verify_oneview_version(self, mock_get_oneview_version):
        mock_get_oneview_version.return_value = {
            'minimumVersion': 120,
            'currentVersion': 200
        }
        self.oneview_client.verify_oneview_version()
        mock_get_oneview_version.assert_called_once_with()

    @mock.patch.object(client.Client, 'get_oneview_version')
    def test_verify_oneview_version_under_supported(self,
                                                    mock_get_oneview_version):
        mock_get_oneview_version.return_value = {
            'minimumVersion': 120,
            'currentVersion': 120
        }
        self.assertRaises(
            exceptions.IncompatibleOneViewAPIVersion,
            self.oneview_client.verify_oneview_version
        )

    @mock.patch.object(client.Client, 'get_oneview_version')
    def test_verify_oneview_version_within_supported(
        self,
        mock_get_oneview_version
    ):
        mock_get_oneview_version.return_value = {
            'minimumVersion': 120,
            'currentVersion': 300
        }
        self.oneview_client.verify_oneview_version()
        mock_get_oneview_version.assert_called_once_with()

    @mock.patch.object(client.Client, 'get_oneview_version')
    def test_verify_oneview_version_within_supported2(
        self,
        mock_get_oneview_version
    ):
        mock_get_oneview_version.return_value = {
            'minimumVersion': 200,
            'currentVersion': 300
        }
        self.oneview_client.verify_oneview_version()
        mock_get_oneview_version.assert_called_once_with()

    @mock.patch.object(client.Client, 'get_oneview_version')
    def test_verify_oneview_version_over_supported(self,
                                                   mock_get_oneview_version):
        mock_get_oneview_version.return_value = {
            'minimumVersion': 300,
            'currentVersion': 400
        }
        self.assertRaises(
            exceptions.IncompatibleOneViewAPIVersion,
            self.oneview_client.verify_oneview_version
        )

    @mock.patch.object(client.Client, 'get_oneview_version')
    def test_verify_oneview_version_not_authorized(self,
                                                   mock_get_oneview_version):
        mock_get_oneview_version.side_effect = [
            exceptions.OneViewNotAuthorizedException
        ]

        self.assertRaises(
            exceptions.OneViewNotAuthorizedException,
            self.oneview_client.verify_oneview_version
        )

    @mock.patch.object(requests, 'get')
    def test_get_oneview_version_forbidden_with_json(self, mock_get):
        response = mock_get.return_value
        response.status_code = http_client.FORBIDDEN
        response.json.return_value = {
            'errorSource': None,
            'recommendedActions': [
                'Check the request URI, then resend the request.'
            ],
            'nestedErrors': [],
            'errorCode': 'GENERIC_HTTP_403',
            'details': 'You are not allowed to access the requested resource.',
            'message': 'Forbidden',
            'data': {}
        }
        mock_get.return_value = response
        self.assertRaises(
            exceptions.OneViewNotAuthorizedException,
            self.oneview_client.get_oneview_version
        )

    @mock.patch.object(requests, 'get')
    def test_get_oneview_version_forbidden_without_json(self, mock_get):
        response = mock_get.return_value
        response.status_code = http_client.FORBIDDEN
        mock_get.return_value = response
        self.assertRaises(
            exceptions.OneViewNotAuthorizedException,
            self.oneview_client.get_oneview_version
        )

    @mock.patch.object(client.Client, 'get_server_profile_from_hardware')
    def test_is_mac_compatible_with_server_profile(
        self, mock_get_server_profile_from_hardware
    ):
        server_profile_mock = models.ServerProfile()
        setattr(
            server_profile_mock,
            'connections',
            [{'boot': {'priority': 'Primary'}, 'mac': 'AA:BB:CC:DD:EE:FF'}]
        )
        setattr(server_profile_mock, 'uri', 'sp_uri')
        mock_get_server_profile_from_hardware.return_value = \
            server_profile_mock

        port = TestablePort('AA:BB:CC:DD:EE:FF')
        node_info = None
        ports = [port]
        self.oneview_client.is_node_port_mac_compatible_with_server_profile(
            node_info, ports)

    @mock.patch.object(client.Client, 'get_server_profile_from_hardware')
    def test_is_mac_compatible_with_server_profile_with_no_ports(
            self, mock_get_server_profile_from_hardware):
        server_profile_mock = models.ServerProfile()
        setattr(
            server_profile_mock,
            'connections',
            [{'boot': {'priority': 'Primary'}, 'mac': 'AA:BB:CC:DD:EE:FF'}]
        )
        setattr(server_profile_mock, 'uri', 'sp_uri')
        mock_get_server_profile_from_hardware.return_value = \
            server_profile_mock

        node_info = None
        ports = []
        self.assertRaises(
            exceptions.OneViewInconsistentResource,
            self.oneview_client
            .is_node_port_mac_compatible_with_server_profile,
            node_info,
            ports
        )

    @mock.patch.object(client.Client, 'get_server_profile_from_hardware')
    def test_is_mac_compatible_with_server_profile_without_boot_in_connection(
            self, mock_get_server_profile_from_hardware):
        server_profile_mock = models.ServerProfile()
        setattr(server_profile_mock, 'connections', [{}])
        setattr(server_profile_mock, 'uri', 'sp_uri')
        mock_get_server_profile_from_hardware.return_value = \
            server_profile_mock
        node_info = None
        ports = None
        self.assertRaises(
            exceptions.OneViewInconsistentResource,
            self.oneview_client
            .is_node_port_mac_compatible_with_server_profile,
            node_info,
            ports
        )

    @mock.patch.object(client.Client, 'get_sh_mac_from_ilo')
    @mock.patch.object(client.Client, 'get_server_hardware')
    @mock.patch.object(client.Client, 'get_server_profile_from_hardware')
    def test_is_mac_compatible_with_server_profile_without_connections(
        self, mock_get_server_profile_from_hardware,
        mock_get_server_hardware, mock_get_sh_mac_from_ilo,
    ):
        server_profile = models.ServerProfile()
        server_profile.connections = []  # No connections, SP for DL server
        server_profile.uri = 'sp_uri'
        mock_get_server_profile_from_hardware.return_value = server_profile

        server_hardware = models.ServerHardware()
        server_hardware_uuid = 'aaaa-bbbb-cccc'
        server_hardware.uuid = server_hardware_uuid
        server_hardware.mp_host_info = {
            'mpIpAddresses': {'address': '192.168.0.1'}
        }
        mock_get_server_hardware.return_value = server_hardware

        mock_get_sh_mac_from_ilo.return_value = 'aa:bb:cc:dd:ee'

        node_info = {'server_hardware_uri': '/rest/111-222-333'}
        ports = [TestablePort('aa:bb:cc:dd:ee')]
        self.oneview_client.is_node_port_mac_compatible_with_server_profile(
            node_info,
            ports
        )

        mock_get_server_hardware.assert_called_once_with(node_info)
        mock_get_sh_mac_from_ilo.assert_called_once_with(server_hardware_uuid,
                                                         nic_index=0)

    @mock.patch('oneview_client.ilo_utils.collection', autospec=True)
    @mock.patch('oneview_client.ilo_utils.ilo_logout', autospec=True)
    @mock.patch.object(client.Client, '_get_ilo_access')
    @mock.patch.object(requests, 'get')
    def test_get_sh_mac_from_ilo(
        self, mock_get, mock_get_ilo_access, mock_ilo_logout, mock_collection,
    ):
        defined_mac = "aa:bb:cc:dd:ee:ff"
        sh_uuid = 'aaa-bbb-ccc'
        my_host = 'https://my-host'
        key = '123'
        mock_collection.return_value = \
            self._create_collection_for_sh_mac_from_ilo_test()
        mock_get_ilo_access.return_value = (my_host, key)
        mac = self.oneview_client.get_sh_mac_from_ilo(sh_uuid)
        mock_get_ilo_access.assert_called_once_with(sh_uuid)
        mock_ilo_logout.assert_called_once_with(my_host, key)
        self.assertEqual(mac, defined_mac)

    def _create_collection_for_sh_mac_from_ilo_test(self):
        status = 200
        headers = None
        system = {'Type': 'ComputerSystem.0',
                  'HostCorrelation': {'HostMACAddress':
                                      ['aa:bb:cc:dd:ee:ff']}}
        memberuri = 'xpto'

        yield status, headers, system, memberuri

    @mock.patch.object(client.Client, '_wait_for_task_to_complete')
    @mock.patch.object(client.Client, '_prepare_and_do_request')
    @mock.patch.object(client.Client, 'get_server_hardware_by_uuid')
    def test_check_server_hardware_state_profile_applied(
            self, mock_get_server_hardware_by_uuid, mock__prepare_do_request,
            mock__wait_for_task
    ):

        server_hardware = models.ServerHardware()
        server_hardware.uri = '/rest/server-hardware/123456789'
        server_hardware.state = states.ONEVIEW_PROFILE_APPLIED
        mock_get_server_hardware_by_uuid.return_value = server_hardware

        self.oneview_client.get_server_hardware_by_uuid = \
            mock_get_server_hardware_by_uuid

        self.assertEqual(
            states.ONEVIEW_PROFILE_APPLIED,
            self.oneview_client.get_server_hardware_by_uuid('123456789').state
        )

    @mock.patch.object(client.Client, '_wait_for_task_to_complete')
    @mock.patch.object(client.Client, '_prepare_and_do_request')
    @mock.patch.object(client.Client, 'get_server_hardware_by_uuid')
    def test_check_server_hardware_state_applying_profile(
            self, mock_get_server_hardware_by_uuid, mock__prepare_do_request,
            mock__wait_for_task_authenticate
    ):

        server_hardware = models.ServerHardware()
        server_hardware.uri = '/rest/server-hardware/123456789'
        server_hardware.state = states.ONEVIEW_APPLYING_PROFILE
        mock_get_server_hardware_by_uuid.return_value = server_hardware

        self.oneview_client.get_server_hardware_by_uuid = \
            mock_get_server_hardware_by_uuid

        self.assertEqual(
            states.ONEVIEW_APPLYING_PROFILE,
            self.oneview_client.get_server_hardware_by_uuid('123456789').state
        )

    @mock.patch.object(client.Client, '_prepare_and_do_request')
    @mock.patch.object(client.Client, '_wait_for_task_to_complete')
    def test_clone_template_and_apply_assignment_with_missing_parameters(
        self, mock__wait_task, mock__prepare
    ):

        self.assertRaises(
            ValueError,
            self.oneview_client.clone_template_and_apply,
            None,
            None,
            None
        )

    @mock.patch.object(client.Client, '_prepare_and_do_request')
    @mock.patch.object(client.Client, '_wait_for_task_to_complete')
    def test_clone_template_and_apply_assignment_error(
        self, mock__wait_task, mock__prepare
    ):

        server_hardware_uuid = '111111111-2222-3333-4444-55555555555'
        server_profile_template_uuid = '555555555-4444-3333-2222-11111111'

        mock__wait_task.side_effect = exceptions.OneViewTaskError
        self.oneview_client._wait_for_task_to_complete = mock__wait_task

        self.assertRaises(
            exceptions.OneViewServerProfileAssignmentError,
            self.oneview_client.clone_template_and_apply,
            'profilename',
            server_hardware_uuid,
            server_profile_template_uuid
        )

    @mock.patch.object(client.Client, '_prepare_and_do_request')
    @mock.patch.object(client.Client, '_wait_for_task_to_complete')
    @mock.patch.object(client.Client, 'get_server_profile_by_uuid')
    def test_clone_template_and_apply_assignment(
        self, mock_get_server_profile_by_uuid, mock__wait_task,
        mock__prepare
    ):

        server_profile_name = 'Ironic Server Profile Test'
        server_hardware_uuid = '111111111-2222-3333-4444-55555555555'
        server_hardware_uri = '/rest/server-hardware/' + \
            server_hardware_uuid
        server_profile_template_uuid = '555555555-4444-3333-2222-11111111'
        server_profile_template_uri = '/rest/server-profile-templates/' + \
            server_profile_template_uuid

        first_server_profile_json = {
            'serverHardwareUri': "/rest/server-hardware/1111-2222-3333",
            'name': "XXXXXXXXXXXXXX",
            'serverProfileTemplateUri': server_profile_template_uri
        }

        mock__prepare.return_value = first_server_profile_json

        second_server_profile_json = {
            'serverHardwareUri': server_hardware_uri,
            'name': server_profile_name,
            'serverProfileTemplateUri': ""
        }

        self.oneview_client.clone_template_and_apply(
            server_profile_name,
            server_hardware_uuid,
            server_profile_template_uuid
        )

        mock__prepare.assert_called_with(
            uri=client.SERVER_PROFILE_PREFIX_URI,
            body=second_server_profile_json,
            request_type=client.POST_REQUEST_TYPE
        )

    @mock.patch.object(client.Client, '_wait_for_task_to_complete')
    @mock.patch.object(client.Client, '_prepare_and_do_request')
    @mock.patch.object(client.Client, 'get_server_hardware')
    def test_delete_server_profile_from_sh_with_missing_profile_uuid(
        self, mock_get_server_hardware, mock__prepare_do_request,
        mock__wait_for_task
    ):

        self.oneview_client._prepare_and_do_request = mock__prepare_do_request
        self.oneview_client._wait_for_task_to_complete = mock__wait_for_task

        self.assertRaises(
            ValueError,
            self.oneview_client.delete_server_profile,
            None
        )

    @mock.patch.object(client.Client, '_wait_for_task_to_complete')
    @mock.patch.object(client.Client, '_prepare_and_do_request')
    @mock.patch.object(client.Client, 'get_server_hardware')
    def test_delete_server_profile_from_sh_unassignment_error(
        self, mock_get_server_hardware, mock__prepare_do_request,
        mock__wait_for_task
    ):

        profile_to_be_deleted_uuid = '111111111-2222-3333-4444-55555555555'

        fake_server_hardware = models.ServerHardware()
        fake_server_hardware.server_profile_uri = \
            '111111111-2222-3333-4444-55555555555'
        mock_get_server_hardware.return_value = fake_server_hardware
        self.oneview_client.get_server_hardware = mock_get_server_hardware

        mock__wait_for_task.side_effect = exceptions.OneViewTaskError
        self.oneview_client._wait_for_task_to_complete = mock__wait_for_task

        self.assertRaises(
            exceptions.OneViewServerProfileDeletionError,
            self.oneview_client.delete_server_profile,
            profile_to_be_deleted_uuid
        )

    @mock.patch.object(client.Client, '_wait_for_task_to_complete')
    @mock.patch.object(client.Client, '_prepare_and_do_request')
    @mock.patch.object(client.Client, 'get_server_hardware')
    def test_delete_server_profile_from_sh(
        self, mock_get_server_hardware, mock__prepare_do_request,
        mock__wait_for_task
    ):

        profile_to_be_deleted_uuid = '111111111-2222-3333-4444-55555555555'

        fake_server_hardware = models.ServerHardware()
        fake_server_hardware.server_profile_uri = \
            '111111111-2222-3333-4444-55555555555'
        mock_get_server_hardware.return_value = fake_server_hardware
        self.oneview_client.get_server_hardware = mock_get_server_hardware

        self.oneview_client._prepare_and_do_request = mock__prepare_do_request
        self.oneview_client._wait_for_task_to_complete = mock__wait_for_task

        self.oneview_client.delete_server_profile(profile_to_be_deleted_uuid)

        self.assertTrue(mock__prepare_do_request.called)
        self.assertTrue(mock__wait_for_task.called)

if __name__ == '__main__':
    unittest.main()
