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

PROPERTIES_DICT = {"cpu_arch": "x86_64",
                   "cpus": "8",
                   "local_gb": "10",
                   "memory_mb": "4096",
                   "capabilities": "server_hardware_type_uri:fake_sht_uri,"
                                   "enclosure_group_uri:fake_eg_uri"}

DRIVER_INFO_DICT = {'server_hardware_uri': 'fake_sh_uri',
                    'server_profile_template_uri': 'fake_spt_uri'}

PORT_MAP = {
    "deviceSlots": [{
        "deviceName": "HP FlexFabric 10Gb 2-port 554FLB Adapter",
        "deviceNumber": 9,
        "location": "Flb",
        "physicalPorts": [{
            "interconnectPort": 1,
            "interconnectUri": ("/rest/interconnects/25352bd0-6a7a-4c1"
                                "d-abe1-268c306c82b8"),
            "mac": "D8:9D:67:73:54:00",
            "physicalInterconnectPort": 1,
            "physicalInterconnectUri": ("/rest/interconnects/25352bd0-"
                                        "6a7a-4c1d-abe1-268c306c82b8"),
            "portNumber": 1,
            "type": "Ethernet",
            "virtualPorts": [{
                "currentAllocatedVirtualFunctionCount": (-1),
                "mac": "EA:EF:C7:70:00:00",
                "portFunction": "a",
                "portNumber": 1,
                "wwnn": None,
                "wwpn": None
            }, {
                "currentAllocatedVirtualFunctionCount": (-1),
                "mac": "D8:9D:67:73:54:01",
                "portFunction": "b",
                "portNumber": 2,
                "wwnn": "20:00:D8:9D:67:73:54:01",
                "wwpn": "10:00:D8:9D:67:73:54:01"
            }, {
                "currentAllocatedVirtualFunctionCount": (-1),
                "mac": "D8:9D:67:73:54:02",
                "portFunction": "c",
                "portNumber": 3,
                "wwnn": None,
                "wwpn": None
            }, {
                "currentAllocatedVirtualFunctionCount": (-1),
                "mac": "D8:9D:67:73:54:03",
                "portFunction": "d",
                "portNumber": 4,
                "wwnn": None,
                "wwpn": None
            }],
            "wwn": None
        }, {
            "interconnectPort": 1,
            "interconnectUri": ("/rest/interconnects/e005478c-8b50-45c"
                                "7-8aae-7239df039078"),
            "mac": "D8:9D:67:73:54:04",
            "physicalInterconnectPort": 1,
            "physicalInterconnectUri": ("/rest/interconnects/e005478c-"
                                        "8b50-45cf-8aae-7239df039078"),
            "portNumber": 2,
            "type": "Ethernet",
            "virtualPorts": [{
                "currentAllocatedVirtualFunctionCount": (-1),
                "mac": "D8:9D:67:73:54:04",
                "portFunction": "a",
                "portNumber": 1,
                "wwnn": None,
                "wwpn": None
            }, {
                "currentAllocatedVirtualFunctionCount": (-1),
                "mac": "D8:9D:67:73:54:05",
                "portFunction": "b",
                "portNumber": 2,
                "wwnn": "20:00:D8:9D:67:73:54:05",
                "wwpn": "10:00:D8:9D:67:73:54:05"
            }, {
                "currentAllocatedVirtualFunctionCount": (-1),
                "mac": "D8:9D:67:73:54:06",
                "portFunction": "c",
                "portNumber": 3,
                "wwnn": None,
                "wwpn": None
            }, {
                "currentAllocatedVirtualFunctionCount": (-1),
                "mac": "D8:9D:67:73:54:07",
                "portFunction": "d",
                "portNumber": 4,
                "wwnn": None,
                "wwpn": None
            }],
            "wwn": None
        }],
        "slotNumber": 1
    }, {
        "deviceName": "HP LPe1205A 8Gb FC HBA for BladeSystem c-Class",
        "deviceNumber": 1,
        "location": "Mezz",
        "physicalPorts": [{
            "interconnectPort": 1,
            "interconnectUri": ("/rest/interconnects/efb60cdf-caf4-438"
                                "2-8419-7ac969504034"),
            "mac": None,
            "physicalInterconnectPort": 1,
            "physicalInterconnectUri": ("/rest/interconnects/efb60cdf-"
                                        "caf4-4382-8419-7ac969504034"),
            "portNumber": 1,
            "type": "FibreChannel",
            "virtualPorts": [],
            "wwn": "10:00:38:EA:A7:D3:E4:40"
        }, {
            "interconnectPort": 1,
            "interconnectUri": ("/rest/interconnects/e4607445-0571-484"
                                "e-8629-8e01bdd1ea9f"),
            "mac": None,
            "physicalInterconnectPort": 1,
            "physicalInterconnectUri": ("/rest/interconnects/e4607445-"
                                        "0571-484e-8629-8e01bdd1ea9f"),
            "portNumber": 2,
            "type": "FibreChannel",
            "virtualPorts": [],
            "wwn": "10:00:38:EA:A7:D3:E4:41"
        }],
        "slotNumber": 1
    }, {
        "deviceName": "",
        "deviceNumber": 2,
        "location": "Mezz",
        "physicalPorts": [],
        "slotNumber": 2
    }]
}


class TestablePort(object):

    def __init__(self, obj_address):
        self.obj_address = obj_address
        self._obj_address = obj_address


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
    def test_power_on_server_off(self, mock_get_pstate, mock_set_pstate):
        driver_info = {"server_hardware_uri": "/any"}
        mock_get_pstate.return_value = states.ONEVIEW_POWER_OFF
        self.oneview_client.power_on(driver_info)
        mock_get_pstate.assert_called_once_with(
            self.oneview_client, driver_info
        )
        mock_set_pstate.assert_called_once_with(
            self.oneview_client, driver_info, states.ONEVIEW_POWER_ON
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
    def test_power_off_server_on(self, mock_get_pstate, mock_set_pstate):
        driver_info = {"server_hardware_uri": "/any"}
        mock_get_pstate.return_value = states.ONEVIEW_POWER_ON
        self.oneview_client.power_off(driver_info)
        mock_get_pstate.assert_called_once_with(
            self.oneview_client, driver_info
        )
        mock_set_pstate.assert_called_once_with(
            self.oneview_client, driver_info, states.ONEVIEW_POWER_OFF,
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
    def test_set_power_state_server_hardware_power_status_error(
        self, mock_get_node_power, mock__prepare_do_request
    ):
        power = states.ONEVIEW_ERROR
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

    @mock.patch.object(client.Client, '_wait_for_task_to_complete',
                       autospec=True)
    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    @mock.patch.object(client.Client, 'get_server_profile_from_hardware',
                       autospec=True)
    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    def test_set_boot_device(
        self, mock_get_server_hardware, mock_get_server_profile,
        mock__prepare_do_request, mock__wait_for_task
    ):
        mock_get_server_hardware.return_value = (
            models.ServerHardware.from_json(fixtures.SERVER_HARDWARE_JSON)
        )
        mock_get_server_profile.return_value = (
            models.ServerProfile.from_json(fixtures.SERVER_PROFILE_JSON)
        )
        expected_profile = copy.deepcopy(fixtures.SERVER_PROFILE_JSON)
        expected_profile['boot'] = {
            'manageBoot': True,
            'order': ["USB", "CD", "Floppy", "HardDisk", "PXE"]
        }
        driver_info = {"server_hardware_uri": "/any"}
        new_first_boot_device = "USB"

        self.oneview_client.set_boot_device(driver_info, new_first_boot_device)
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
    @mock.patch.object(client.Client, 'get_boot_order', autospec=True)
    def test_get_server_profile_from_hardware(
        self, mock_get_boot_order, mock_get_server_hardware,
        mock__prepare_do_request
    ):
        driver_info = {}
        new_first_boot_device = "any_boot_device"
        mock_get_boot_order.return_value = []
        server_hardware = models.ServerHardware()
        setattr(server_hardware, 'server_profile_uri', None)
        mock_get_server_hardware.return_value = server_hardware

        self.assertRaises(
            exceptions.OneViewServerProfileAssociatedError,
            self.oneview_client.set_boot_device,
            driver_info,
            new_first_boot_device
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
            self.oneview_client.set_boot_device,
            driver_info,
            new_first_boot_device
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

    @mock.patch.object(client.Client, '_authenticate', autospec=True)
    @mock.patch.object(client.Client, '_prepare_and_do_request', autospec=True)
    def test__wait_for_task_to_complete(self, mock__prepare_do_request,
                                        mock__authenticate):

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

        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password,
                                       max_polling_attempts=1)

        mock__prepare_do_request.side_effect = [task1, task2, task3]
        oneview_client._wait_for_task_to_complete(task0)

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
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password,
                                       max_polling_attempts=2)

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
    def test_validate_node_server_hardware_inconsistent_cpus_value(
        self, mock_get_server_hardware
    ):
        server_hardware_mock = models.ServerHardware()
        setattr(server_hardware_mock, "processor_core_count", 2)
        setattr(server_hardware_mock, "processor_count", 3)
        setattr(server_hardware_mock, "memory_mb", 1)

        mock_get_server_hardware.return_value = server_hardware_mock

        driver_info = {
            "server_hardware_uri": "/any_uri",
        }
        node_memorymb = 1
        node_cpus = 3

        exc_expected_msg = (
            "Node cpus is inconsistent with OneView's server"
            " hardware /any_uri cpus."
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
        server_hardware_mock_port_map = PORT_MAP
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
        server_hardware_mock_port_map = PORT_MAP
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
    def test_check_node_port_mac_no_primary_boot_connection(
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

    @mock.patch.object(client.Client, 'get_server_profile_template',
                       autospec=True)
    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    def test_validate_node_server_profile_template_inconsistent_sht(
        self, mock_server_hardware, mock_server_template
    ):
        server_hardware_mock = models.ServerHardware()
        setattr(server_hardware_mock,
                "server_hardware_type_uri",
                "/sht_uri")
        setattr(server_hardware_mock, "enclosure_group_uri", "eg_uri")

        server_profile_template_mock = models.ServerProfileTemplate()
        setattr(server_profile_template_mock,
                "server_hardware_type_uri",
                "/inconsistent_uri")
        setattr(server_profile_template_mock,
                "enclosure_group_uri",
                "/inconsistent_uri")

        mock_server_hardware.return_value = server_hardware_mock
        mock_server_template.return_value = server_profile_template_mock

        driver_info = {
            "server_hardware_uri": "/any_uri",
            "server_profile_template_uri": "/profile_uri"
        }

        exc_expected_msg = (
            "Server profile template /profile_uri serverHardwareTypeUri is"
            " inconsistent with server hardware /any_uri"
            " serverHardwareTypeUri."
        )

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            self.oneview_client.validate_node_server_profile_template,
            driver_info
        )

    @mock.patch.object(client.Client, 'get_server_profile_template',
                       autospec=True)
    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    def test_validate_node_server_profile_template_inconsistent_eg(
        self, mock_server_hardware, mock_server_template
    ):
        server_hardware_mock = models.ServerHardware()
        setattr(server_hardware_mock,
                "server_hardware_type_uri",
                "/sht_uri")
        setattr(server_hardware_mock, "enclosure_group_uri", "eg_uri")

        server_profile_template_mock = models.ServerProfileTemplate()
        setattr(server_profile_template_mock,
                "server_hardware_type_uri",
                "/sht_uri")
        setattr(server_profile_template_mock,
                "enclosure_group_uri",
                "/inconsistent_uri")

        mock_server_hardware.return_value = server_hardware_mock
        mock_server_template.return_value = server_profile_template_mock

        driver_info = {
            "server_hardware_uri": "/any_uri",
            "server_profile_template_uri": "/profile_uri"
        }

        exc_expected_msg = (
            "Server profile template /profile_uri enclosureGroupUri is"
            " inconsistent with server hardware /any_uri"
            " serverGroupUri."
        )

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            self.oneview_client.validate_node_server_profile_template,
            driver_info
        )

    @mock.patch.object(client.Client, 'get_server_profile_template',
                       autospec=True)
    @mock.patch.object(client.Client, 'get_server_hardware', autospec=True)
    def test_validate_node_server_profile_template_no_primary_boot_connection(
        self, mock_server_hardware, mock_server_template
    ):
        server_hardware_mock = models.ServerHardware()
        setattr(server_hardware_mock, "server_hardware_type_uri", "/sht_uri")
        setattr(server_hardware_mock, "enclosure_group_uri", "/eg_uri")

        profile_template_mock = models.ServerProfileTemplate()
        setattr(profile_template_mock, "uri", "/template_uri")
        setattr(profile_template_mock, "server_hardware_type_uri", "/sht_uri")
        setattr(profile_template_mock, "enclosure_group_uri", "/eg_uri")

        profile_template_mock_connections = [
            {'boot': {'priority': u'NotBootable'},
             'mac': u'56:88:7B:C0:00:0B'}
        ]
        setattr(profile_template_mock,
                "connections",
                profile_template_mock_connections)

        mock_server_template.return_value = profile_template_mock
        mock_server_hardware.return_value = server_hardware_mock

        exc_expected_msg = (
            "No primary boot connection configured for server profile"
            " template /template_uri."
        )

        driver_info = {
            "server_profile_template_uri": "/profile_uri"
        }

        self.assertRaisesRegexp(
            exceptions.OneViewInconsistentResource,
            exc_expected_msg,
            self.oneview_client
            .validate_node_server_profile_template,
            driver_info
        )

    @mock.patch.object(client.Client, 'get_oneview_version')
    def test_verify_oneview_version(self, mock_get_oneview_version):
        mock_get_oneview_version.return_value = {
            'minimumVersion': 120,
            'currentVersion': 200
        }
        self.oneview_client.verify_oneview_version()
        mock_get_oneview_version.assert_called_once_with()

    @mock.patch.object(client.Client, 'get_oneview_version')
    def test_verify_oneview_version_fail(self, mock_get_oneview_version):
        mock_get_oneview_version.return_value = {
            'minimumVersion': 120,
            'currentVersion': 120
        }
        self.assertRaises(
            exceptions.IncompatibleOneViewAPIVersion,
            self.oneview_client.verify_oneview_version
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
            self.create_collection_for_sh_mac_from_ilo_test()
        mock_get_ilo_access.return_value = (my_host, key)
        mac = self.oneview_client.get_sh_mac_from_ilo(sh_uuid)
        mock_get_ilo_access.assert_called_once_with(sh_uuid)
        mock_ilo_logout.assert_called_once_with(my_host, key)
        self.assertEqual(mac, defined_mac)

    def create_collection_for_sh_mac_from_ilo_test(self):
        status = 200
        headers = None
        system = {'Type': 'ComputerSystem.0',
                  'HostCorrelation': {'HostMACAddress':
                                      ['aa:bb:cc:dd:ee:ff']}}
        memberuri = 'xpto'

        yield status, headers, system, memberuri


if __name__ == '__main__':
    unittest.main()
