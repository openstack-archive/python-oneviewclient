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


import mock
import requests
import retrying
import unittest

from oslo_config import cfg
from oslo_config import types

from oneview_client import client as oneview_client
from oneview_client import exceptions
from oneview_client import states

opts = [
    cfg.StrOpt('manager_url',
               help='URL where OneView is available'),
    cfg.StrOpt('username',
               help='OneView username to be used'),
    cfg.StrOpt('password',
               help='OneView password to be used'),
    cfg.StrOpt('nova_username',
               help='Nova username'),
    cfg.StrOpt('nova_user_pass',
               help='Nova password'),
    cfg.StrOpt('nova_user_tenant',
               help='Nova user tenant'),
    cfg.Opt('allow_insecure_connections',
            type=types.Boolean(),
            default=False,
            help='Option to allow insecure connection with OneView'),
    cfg.StrOpt('tls_cacert_file',
               default=None,
               help='Path to CA certificate'),
    cfg.IntOpt('max_polling_attempts',
               default=20,
               help='Max connection retries to check changes on OneView'),
]

CONF = cfg.CONF
CONF.register_opts(opts, group='oneview')

PROPERTIES_DICT = {"cpu_arch": "x86_64",
                   "cpus": "8",
                   "local_gb": "10",
                   "memory_mb": "4096",
                   "capabilities": "server_hardware_type_uri:fake_sht_uri,"
                                   "enclosure_group_uri:fake_eg_uri"}

DRIVER_INFO_DICT = {'server_hardware_uri': 'fake_sh_uri',
                    'server_profile_template_uri': 'fake_spt_uri'}


class OneViewClientTestCase(unittest.TestCase):

    def setUp(self):
        super(OneViewClientTestCase, self).setUp()
        self.config(manager_url='https://1.2.3.4', group='oneview')
        self.config(username='user', group='oneview')
        self.config(password='password', group='oneview')

    def config(self, **kw):
        """Override config options for a test."""
        group = kw.pop('group', None)
        for k, v in kw.items():
            CONF.set_override(k, v, group)

    @mock.patch.object(oneview_client, '_wait_for_task_to_complete',
                       autospec=True)
    @mock.patch.object(oneview_client, 'prepare_and_do_request', autospec=True)
    @mock.patch.object(oneview_client, 'get_node_power_state', autospec=True)
    def test_set_power_on_server_hardware(self, mock_get_node_power,
                                          mock_prepare_do_request,
                                          mock__wait_for_task):
        power_on = states.POWER_ON
        mock_get_node_power.return_value = power_on
        mock_prepare_do_request.return_value = {}
        driver_info = {"server_hardware_uri": "/any"}
        target_state = "On"

        current_state = oneview_client.set_node_power_state(driver_info,
                                                            target_state)
        self.assertEqual(current_state, power_on)

    @mock.patch.object(oneview_client, 'get_authentication', autospec=True)
    @mock.patch.object(requests, 'put', autospec=True)
    def test_set_power_on_server_hardware_nonexistent(
            self, mock_do_request, mock_get_authentication):

        class Response(object):
            status_code = 404

            def json(self):
                return {
                    "errorCode": "RESOURCE_NOT_FOUND",
                    "details": "Resource not found, ID = /any_invalid",
                }

        mock_do_request.return_value = Response()

        driver_info = {"server_hardware_uri": "/any_invalid"}
        target_state = states.POWER_ON

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client.set_node_power_state, driver_info, target_state
        )

    @mock.patch.object(oneview_client, 'prepare_and_do_request', autospec=True)
    @mock.patch.object(oneview_client, 'get_node_power_state', autospec=True)
    def test_set_power_on_server_hardware_power_status_error(
            self, mock_get_node_power, mock_prepare_do_request):
        power = states.ERROR
        mock_get_node_power.return_value = power
        mock_prepare_do_request.return_value = {
            "taskState": "Error",
            "percentComplete": 100
        }
        driver_info = {"server_hardware_uri": "/any"}
        target_state = "On"

        self.assertRaises(
            exceptions.OneViewErrorStateSettingPowerState,
            oneview_client.set_node_power_state, driver_info, target_state
        )

    @mock.patch.object(oneview_client, 'prepare_and_do_request', autospec=True)
    def test_get_server_hardware_nonexistent(self, mock_prepare_do_request):
        mock_prepare_do_request.return_value = {"error": "resource not found"}
        driver_info = {"server_hardware_uri": ""}
        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client.get_server_hardware,
            driver_info
        )

    @mock.patch.object(oneview_client, 'get_authentication', autospec=True)
    def test_invalid_login_password_credentials(self, mock_get_authentication):
        mock_get_authentication.return_value = None
        self.assertRaises(
            exceptions.OneViewNotAuthorizedException,
            oneview_client.prepare_and_do_request,
            '/any'
        )

    @mock.patch.object(oneview_client, 'prepare_and_do_request', autospec=True)
    @mock.patch.object(oneview_client, 'get_server_profile_from_hardware',
                       autospec=True)
    def test_set_boot_device_nonexistent_resource_uri(self,
                                                      mock_get_server_profile,
                                                      mock_prepare_do_request):
        driver_info = {}
        new_first_boot_device = "None"
        mock_prepare_do_request.return_value = {
            "errorCode": "RESOURCE_NOT_FOUND",
            "data": None
        }

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client.set_boot_device,
            driver_info,
            new_first_boot_device
        )

    @mock.patch.object(oneview_client, 'get_boot_order', autospec=True)
    def test_set_boot_device_nonexistent_resource_first_boot_device(
            self,
            mock_get_boot_order):
        driver_info = {}
        new_first_boot_device = None
        mock_get_boot_order.return_value = []

        self.assertRaises(
            exceptions.OneViewBootDeviceInvalidError,
            oneview_client.set_boot_device,
            driver_info,
            new_first_boot_device
        )

    @mock.patch.object(oneview_client, 'prepare_and_do_request', autospec=True)
    @mock.patch.object(oneview_client, 'get_server_hardware', autospec=True)
    @mock.patch.object(oneview_client, 'get_boot_order', autospec=True)
    def test_get_server_profile_from_hardware(self, mock_get_boot_order,
                                              mock_get_server_hardware,
                                              mock_prepare_do_request):
        driver_info = {}
        new_first_boot_device = "any_boot_device"
        mock_get_boot_order.return_value = []
        mock_get_server_hardware.return_value = {}

        self.assertRaises(
            exceptions.OneViewServerProfileAssociatedError,
            oneview_client.set_boot_device,
            driver_info,
            new_first_boot_device
        )

        mock_get_server_hardware.return_value = {"serverProfileUri": "any_uri"}
        mock_prepare_do_request.return_value = {}

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client.set_boot_device,
            driver_info,
            new_first_boot_device
        )

    @mock.patch.object(oneview_client, 'prepare_and_do_request', autospec=True)
    def test__wait_for_task_to_complete(self, mock_prepare_do_request):
        self.config(max_polling_attempts=1, group='oneview')
        task = {
            "uri": "/any_uri",
            "taskState": "Something",
            "percentComplete": 100
        }
        mock_prepare_do_request.return_value = task
        oneview_client._wait_for_task_to_complete(task)

    @mock.patch.object(oneview_client, 'prepare_and_do_request', autospec=True)
    def test__wait_for_task_to_complete_timeout(self, mock_prepare_do_request):
        self.config(max_polling_attempts=1, group='oneview')

        task = {
            "uri": "/any_uri",
            "taskState": "Something",
            "percentComplete": 30
        }

        mock_prepare_do_request.return_value = task
        self.assertRaises(
            retrying.RetryError,
            oneview_client._wait_for_task_to_complete,
            task,
        )

    @mock.patch.object(oneview_client, 'get_server_hardware', autospec=True)
    def test_validate_node_server_hardware_inconsistent_memorymb_value(
        self, mock_get_server_hardware):
        mock_get_server_hardware.return_value = {
            "memoryMb": 1,
            "processorCoreCount": 1,
            "processorCount": 1,
        }
        driver_info = {
            "server_hardware_uri": "/any_uri",
        }
        node_uuid = 12345
        node_memorymb = 2
        node_cpus = 1

        exc_expected_msg = (
            "Node 12345 memory_mb is inconsistent with OneView's server"
            " hardware /any_uri memoryMb. Node validation failed."
        )
        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            oneview_client.validate_node_server_hardware,
            driver_info,
            node_uuid,
            node_memorymb,
            node_cpus
        )

    @mock.patch.object(oneview_client, 'get_server_hardware', autospec=True)
    def test_validate_node_server_hardware_inconsistent_cpus_value(
        self, mock_get_server_hardware):
        mock_get_server_hardware.return_value = {
            "memoryMb": 1,
            "processorCoreCount": 2,
            "processorCount": 3,
        }
        driver_info = {
            "server_hardware_uri": "/any_uri",
        }
        node_uuid = 12345
        node_memorymb = 1
        node_cpus = 3

        exc_expected_msg = (
            "Node 12345 cpus is inconsistent with OneView's server"
            " hardware /any_uri cpus. Node validation failed."
        )
        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            oneview_client.validate_node_server_hardware,
            driver_info,
            node_uuid,
            node_memorymb,
            node_cpus
        )

    def test_validate_node_server_hardware_type_empty_sht_uri(self):
        driver_info = {
            "server_hardware_type_uri": "",
        }
        node_uuid = 12345

        exc_expected_msg = (
            "Node 12345 properties/capabilities server_hardware_type_uri is"
            " empty. Node validation failed."
        )
        self.assertRaisesRegexp(
            exceptions.OneViewResourceNotFoundError,
            exc_expected_msg,
            oneview_client.validate_node_server_hardware_type,
            driver_info,
            node_uuid
        )

    @mock.patch.object(oneview_client, 'get_server_hardware', autospec=True)
    def test_validate_node_server_hardware_type_inconsistent_sht_uri(
        self, mock_get_server_hardware):
        mock_get_server_hardware.return_value = {
            "serverHardwareTypeUri": "/incosistent_uri"
        }
        driver_info = {
            "server_hardware_uri": "/any_serveruri",
            "server_hardware_type_uri": "/any_uri",
        }
        node_uuid = 12345

        exc_expected_msg = (
            "Node 12345 server_hardware_type_uri is inconsistent with"
            " OneView's server hardware /any_serveruri serverHardwareTypeUri."
            " Node validation failed."
        )
        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            oneview_client.validate_node_server_hardware_type,
            driver_info,
            node_uuid
        )

    @mock.patch.object(oneview_client, 'get_server_profile_from_hardware',
                       autospec=True)
    def test_check_server_profile_is_applied_health_status_fail(
        self, mock_server_profile):
        mock_server_profile.return_value = {
            "uri": "/any_uri",
            "status": "Not OK"
        }

        exc_expected_msg = (
            "Server Profile /any_uri health status Not OK indicates"
            " something is wrong. Node validation failed."
        )
        self.assertRaisesRegexp(
            exceptions.OneViewHealthStatusError,
            exc_expected_msg,
            oneview_client.check_server_profile_is_applied,
            {},
        )

    @mock.patch.object(oneview_client, 'get_server_hardware', autospec=True)
    def test_validate_node_enclosure_group_inconsistent(
        self, mock_get_server_hardware):
        driver_info = {
            "server_hardware_uri": "/any_uri",
            "enclosure_group_uri": "/inconsistent_uri"
        }
        node_uuid = 12345

        exc_expected_msg = (
            "Node 12345 enclosure_group_uri is inconsistent with"
            " OneView's server hardware /any_uri serverGroupUri."
            " Node validation failed."
        )
        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            oneview_client.validate_node_enclosure_group,
            driver_info,
            node_uuid
        )

    @mock.patch.object(oneview_client, 'get_server_profile_from_hardware',
                       autospec=True)
    def test_check_node_port_mac_is_compatible_with_server_profile_fail(
        self, mock_server_profile):
        mock_server_profile.return_value = {
            "uri": "/anyuri",
            "connections": [
                {"mac": "56:88:7B:C0:00:0A"}
            ]
        }
        node_uuid = 12345

        exc_expected_msg = (
            "Port of node 12345 is not compatible with applied server"
            " profile /anyuri. Node validation failed."
        )
        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            oneview_client
            .check_node_port_mac_is_compatible_with_server_profile,
            {},
            {},
            node_uuid
        )

    def test_validate_node_server_profile_template_empty_spt_uri(self):
        driver_info = {
            "server_hardware_uri": "/any_uri",
            "server_profile_template_uri": ""
        }
        node_uuid = 12345

        exc_expected_msg = (
            "Node 12345 driver_info/server_profile_template_uri is"
            " empty. Node validation failed."
        )
        self.assertRaisesRegexp(
            exceptions.OneViewResourceNotFoundError,
            exc_expected_msg,
            oneview_client.validate_node_server_profile_template,
            driver_info,
            node_uuid
        )

    @mock.patch.object(oneview_client, 'get_server_profile_template',
                       autospec=True)
    @mock.patch.object(oneview_client, 'get_server_hardware', autospec=True)
    def test_validate_node_server_profile_template_inconsistent_sht(
        self, mock_server_hardware, mock_server_template):
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
        node_uuid = 12345

        exc_expected_msg = (
            "Server profile template /profile_uri serverHardwareTypeUri is"
            " inconsistent with server hardware /any_uri"
            " serverHardwareTypeUri. Node validation failed."
        )
        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            oneview_client.validate_node_server_profile_template,
            driver_info,
            node_uuid
        )

    @mock.patch.object(oneview_client, 'get_server_profile_template',
                       autospec=True)
    @mock.patch.object(oneview_client, 'get_server_hardware', autospec=True)
    def test_validate_node_server_profile_template_inconsistent_eg(
        self, mock_server_hardware, mock_server_template):
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
        node_uuid = 12345

        exc_expected_msg = (
            "Server profile template /profile_uri enclosureGroupUri is"
            " inconsistent with server hardware /any_uri"
            " serverGroupUri. Node validation failed."
        )
        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            oneview_client.validate_node_server_profile_template,
            driver_info,
            node_uuid
        )
