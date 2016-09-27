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
import six.moves.http_client as http_client
import unittest

from oneview_client import client
from oneview_client import exceptions
from oneview_client import ilo_utils
from oneview_client import models
from oneview_client.tests import fixtures
from oneview_client import utils


class OneViewClientAuthTestCase(unittest.TestCase):

    def setUp(self):
        super(OneViewClientAuthTestCase, self).setUp()
        self.manager_url = 'https://1.2.3.4'
        self.username = 'user'
        self.password = 'password'

    @mock.patch.object(requests, 'delete', autospec=True)
    @mock.patch.object(requests, 'get', autospec=True)
    @mock.patch.object(requests, 'post', autospec=True)
    def test_re_login(self,
                      mock_post,
                      mock_get,
                      mock_delete):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        response = mock_post.return_value
        response.json.return_value = {'sessionID': 'aaabbb'}
        response.status_code = http_client.OK
        mock_post.return_value = response

        response1 = mock_get.return_value
        response1.status_code = http_client.OK
        response1.json = mock.MagicMock(
            return_value=fixtures.SERVER_HARDWARE_LIST_JSON
        )
        mock_get.return_value = response1

        sh_uuid = oneview_client.server_hardware.list()[0].uuid
        assert sh_uuid
        oneview_client._logout()
        mock_post.reset_mock()

        response2 = mock.Mock(status_code=http_client.UNAUTHORIZED)
        response3 = mock.Mock(status_code=http_client.OK)
        mock_get.side_effect = [response2, response3]

        oneview_client.server_hardware.get(sh_uuid)
        mock_post.assert_called_once_with(
            'https://1.2.3.4/rest/login-sessions',
            data=json.dumps({"userName": "user", "password": "password"}),
            headers={'content-type': 'application/json'},
            verify=True
        )

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


@mock.patch.object(client.Client, '_authenticate', autospec=True)
class OneViewClientTestCase(unittest.TestCase):

    def setUp(self):
        super(OneViewClientTestCase, self).setUp()
        self.manager_url = 'https://1.2.3.4'
        self.username = 'user'
        self.password = 'password'

    @mock.patch.object(requests, 'get', autospec=True)
    def test_get_server_hardware(self, mock_get, mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=fixtures.SERVER_HARDWARE_JSON
        )
        mock_get.return_value = response

        node_info = {
            'server_hardware_uri': '/rest/server-hardware/aaaa-bbbb-cccc'
        }

        sh = oneview_client.get_server_hardware(node_info)

        mock_get.assert_called_once_with(
            url='https://1.2.3.4/rest/server-hardware/aaaa-bbbb-cccc',
            headers=mock.ANY,
            verify=True
        )
        self.assertIsInstance(sh, models.ServerHardware)

    @mock.patch.object(requests, 'get', autospec=True)
    def test_get_server_hardware_not_found(self, mock_get, mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        response = mock_get.return_value
        response.status_code = http_client.NOT_FOUND
        mock_get.return_value = response

        node_info = {
            'server_hardware_uri': '/rest/server-hardware/aaaa-bbbb-cccc'
        }

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client.get_server_hardware,
            node_info
        )

    @mock.patch.object(requests, 'get', autospec=True)
    def test_get_server_profile_template(self, mock_get, mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=fixtures.SERVER_PROFILE_TEMPLATE_JSON
        )
        mock_get.return_value = response

        node_info = {
            'server_profile_template_uri':
                '/rest/server-profile-templates/aaaa-bbbb-cccc'
        }

        spt = oneview_client.get_server_profile_template(node_info)
        mock_get.assert_called_once_with(
            url='https://1.2.3.4/rest/server-profile-templates/aaaa-bbbb-cccc',
            headers=mock.ANY,
            verify=True
        )
        self.assertIsInstance(spt, models.ServerProfileTemplate)

    @mock.patch.object(requests, 'get', autospec=True)
    def test_get_server_profile_template_not_found(self, mock_get,
                                                   mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        response = mock_get.return_value
        response.status_code = http_client.NOT_FOUND
        mock_get.return_value = response

        node_info = {
            'server_profile_template_uri':
                '/rest/server-profile-templates/aaaa-bbbb-cccc'
        }

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client.get_server_profile_template,
            node_info
        )

    @mock.patch.object(requests, 'get', autospec=True)
    def test_get_server_profile_from_hardware(self, mock_get,
                                              mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        hardware = mock.MagicMock()
        hardware.status_code = http_client.OK
        hardware.json = mock.MagicMock(
            return_value=fixtures.SERVER_HARDWARE_LIST_JSON['members'][0]
        )
        profile = mock.MagicMock()
        profile.status_code = http_client.OK
        profile_fixture = copy.deepcopy(fixtures.SERVER_PROFILE_JSON)
        profile.json = mock.MagicMock(
            return_value=profile_fixture
        )
        mock_get.side_effect = [hardware, profile]

        node_info = {
            'server_hardware_uri':
                '/rest/server-hardware/30303437-3933-4753-4831-31315835524E'
        }

        sp = oneview_client.get_server_profile_from_hardware(node_info)
        mock_get.assert_has_calls(
            [mock.call(
                url='https://1.2.3.4/rest/server-hardware/30303437-3933-4753-4'
                    '831-31315835524E',
                headers=mock.ANY,
                verify=True,
            ), mock.call(
                url='https://1.2.3.4/rest/server-profiles/f2160e28-8107-45f9-b'
                    '4b2-3119a622a3a1',
                headers=mock.ANY,
                verify=True,
            )]
        )
        self.assertIsInstance(sp, models.ServerProfile)

    @mock.patch.object(requests, 'get', autospec=True)
    def test_get_server_profile_from_hardware_no_profile(self, mock_get,
                                                         mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        hardware = mock.MagicMock()
        hardware.status_code = http_client.OK
        hardware.json = mock.MagicMock(
            return_value=fixtures.SERVER_HARDWARE_JSON
        )
        profile = mock.MagicMock()
        profile.status_code = http_client.OK
        profile_fixture = copy.deepcopy(fixtures.SERVER_PROFILE_JSON)
        profile.json = mock.MagicMock(
            return_value=profile_fixture
        )
        mock_get.side_effect = [hardware, profile]

        node_info = {
            'server_hardware_uri':
                '/rest/server-hardware/30303437-3933-4753-4831-31315835524E'
        }

        self.assertRaises(
            exceptions.OneViewServerProfileAssociatedError,
            oneview_client.get_server_profile_from_hardware,
            node_info
        )

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_profile_get_not_found(self, mock_get, mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        response = mock_get.return_value
        response.status_code = http_client.NOT_FOUND
        mock_get.return_value = response

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client._server_profile.get,
            'aaaa-bbbb-cccc'
        )

    def test_server_profile_create(self, mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        self.assertRaises(
            NotImplementedError,
            oneview_client._server_profile.create,
            name='something',
            description='somethingelse',
            something=0
        )

    @mock.patch.object(client.Client, '_wait_for_task_to_complete')
    @mock.patch.object(requests, 'delete', autospec=True)
    def test_delete_server_profile(self,
                                   mock_delete,
                                   mock__wait_for_task,
                                   mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        response = mock_delete.return_value
        response.status_code = http_client.OK
        oneview_client._wait_for_task_to_complete = mock__wait_for_task

        oneview_client.delete_server_profile('1111-2222-3333')

        mock_delete.assert_called_once_with(
            url='https://1.2.3.4/rest/server-profiles/1111-2222-3333',
            headers=mock.ANY,
            verify=True
        )

    @mock.patch.object(requests, 'get', autospec=True)
    def test_validate_node_server_profile_template(
        self, mock_get, mock__authenticate
    ):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        server_profile_template = copy.deepcopy(
            fixtures.SERVER_PROFILE_TEMPLATE_JSON
        )
        server_hardware = copy.deepcopy(fixtures.SERVER_HARDWARE_JSON)
        server_hardware['serverHardwareTypeUri'] = (
            "/rest/server-hardware-types/934E00C0-45F0-4329-AA8C-A0864E834ED4"
        )

        node_info = {
            'server_profile_template_uri':
                server_profile_template.get('uri'),
            'server_hardware_uri':
                server_hardware.get('uri'),
        }

        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock()
        response.json.side_effect = [
            server_profile_template, server_hardware
        ]
        mock_get.return_value = response

        oneview_client.validate_node_server_profile_template(
            node_info
        )

    @mock.patch.object(requests, 'get', autospec=True)
    def test_validate_node_server_profile_template_manage_boot_false(
        self, mock_get, mock__authenticate
    ):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        server_profile_template = copy.deepcopy(
            fixtures.SERVER_PROFILE_TEMPLATE_JSON
        )
        server_profile_template['boot']['manageBoot'] = False

        server_hardware = copy.deepcopy(fixtures.SERVER_HARDWARE_JSON)
        server_hardware['serverHardwareTypeUri'] = (
            "/rest/server-hardware-types/934E00C0-45F0-4329-AA8C-A0864E834ED4"
        )

        node_info = {
            'server_profile_template_uri':
                server_profile_template.get('uri'),
            'server_hardware_uri':
                server_hardware.get('uri'),
        }

        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock()
        response.json.side_effect = [
            server_profile_template, server_hardware
        ]
        mock_get.return_value = response

        self.assertRaises(
            exceptions.OneViewInconsistentResource,
            oneview_client.validate_node_server_profile_template,
            node_info
        )

    @mock.patch.object(requests, 'get', autospec=True)
    def test__validate_server_profile_template_boot_connections(
        self, mock_get, mock__authenticate
    ):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        passes = [
            # Single connection, Primary
            fixtures.SERVER_PROFILE_TEMPLATE_LIST_JSON.get('members')[0],
            # Two connections, Primary first
            fixtures.SERVER_PROFILE_TEMPLATE_LIST_JSON.get('members')[2],
            # Two connections, Primary second
            fixtures.SERVER_PROFILE_TEMPLATE_LIST_JSON.get('members')[3],
        ]

        for spt in passes:
            server_profile_template = models.ServerProfileTemplate.from_json(
                spt
            )
            response = mock_get.return_value
            response.status_code = http_client.OK
            response.json = mock.MagicMock(
                return_value=server_profile_template
            )
            mock_get.return_value = response
            oneview_client._validate_spt_boot_connections(
                server_profile_template
            )

    @mock.patch.object(requests, 'get', autospec=True)
    def test__validate_server_profile_template_boot_connections_fails(
        self, mock_get, mock__authenticate
    ):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        fails = [
            # Single connection, no primary
            fixtures.SERVER_PROFILE_TEMPLATE_LIST_JSON.get('members')[1],
            # Two connections, any primary
            fixtures.SERVER_PROFILE_TEMPLATE_LIST_JSON.get('members')[4],
            # No connections
            fixtures.SERVER_PROFILE_TEMPLATE_LIST_JSON.get('members')[9],
        ]

        for spt in fails:
            server_profile_template = models.ServerProfileTemplate.from_json(
                spt
            )
            response = mock_get.return_value
            response.status_code = http_client.OK
            response.json = mock.MagicMock(
                return_value=server_profile_template
            )
            mock_get.return_value = response
            self.assertRaises(
                exceptions.OneViewInconsistentResource,
                oneview_client._validate_spt_boot_connections,
                server_profile_template
            )

    @mock.patch.object(client.Client, '_wait_for_task_to_complete')
    @mock.patch.object(requests, 'get', autospec=True)
    @mock.patch.object(requests, 'put', autospec=True)
    def test_set_boot_device(self, mock_put, mock_get, mock__wait_for_task,
                             mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        response = mock_put.return_value
        response.status_code = http_client.OK
        mock_put.return_value = response

        hardware = mock.MagicMock()
        hardware.status_code = http_client.OK
        hardware.json = mock.MagicMock(
            return_value=fixtures.SERVER_HARDWARE_LIST_JSON['members'][0]
        )
        profile = mock.MagicMock()
        profile.status_code = http_client.OK
        profile_fixture = copy.deepcopy(fixtures.SERVER_PROFILE_JSON)
        profile.json = mock.MagicMock(
            return_value=profile_fixture
        )
        mock_get.side_effect = [hardware, profile, hardware, profile]
        oneview_client._wait_for_task_to_complete = mock__wait_for_task

        node_info = {
            'server_hardware_uri':
                '/rest/server-hardware/30303437-3933-4753-4831-31315835524E'
        }

        oneview_client.set_boot_device(node_info, 'PXE')
        mock_put.assert_called_once_with(
            self.manager_url + profile_fixture.get('uri'),
            data=mock.ANY,
            headers=mock.ANY,
            verify=True
        )
        self.assertIn('["PXE", "CD", "Floppy", "USB", "HardDisk"]',
                      mock_put.call_args[1]['data'])

    @mock.patch.object(ilo_utils, 'ilo_logout')
    @mock.patch.object(client.Client, '_get_ilo_access')
    @mock.patch.object(client.Client, '_wait_for_task_to_complete')
    @mock.patch.object(requests, 'get', autospec=True)
    @mock.patch.object(requests, 'patch', autospec=True)
    def test_set_boot_device_onetime(self, mock_patch, mock_get,
                                     mock__wait_for_task, mock_get_ilo_access,
                                     mock_ilo_logout, mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        hardware = mock.MagicMock()
        hardware.status_code = http_client.OK
        hardware.json = mock.MagicMock(
            return_value=fixtures.SERVER_HARDWARE_LIST_JSON['members'][0]
        )
        profile = mock.MagicMock()
        profile.status_code = http_client.OK
        profile_fixture = copy.deepcopy(fixtures.SERVER_PROFILE_JSON)
        profile.json = mock.MagicMock(
            return_value=profile_fixture
        )
        ilo_system = mock.MagicMock()
        ilo_system.status_code = http_client.OK
        ilo_system.json = mock.MagicMock(
            return_value={
                "Type": "Collection.0",
                "Items": [
                    {
                        "links": {"self": {"href": "/rest/v1/Systems/1"}},
                        "Type": "ComputerSystem.0",
                        "Boot": {
                            "BootSourceOverrideSupported": ["Hdd", "Cd"],
                        }
                    },
                ]
            }
        )
        mock_get.side_effect = [hardware, profile,  # hardware, profile,
                                ilo_system]

        response2 = mock_patch.return_value
        response2.status_code = http_client.OK
        mock_patch.return_value = response2

        my_host = 'my-host'
        key = '123'
        mock_get_ilo_access.return_value = (my_host, key)

        oneview_client._wait_for_task_to_complete = mock__wait_for_task

        node_info = {
            'server_hardware_uri':
                '/rest/server-hardware/30303437-3933-4753-4831-31315835524E'
        }

        oneview_client.set_boot_device(node_info, 'HardDisk', onetime=True)
        mock_patch.assert_called_once_with(
            'https://' + my_host + '/rest/v1/Systems/1',
            data=json.dumps({"Boot": {"BootSourceOverrideTarget": "Hdd",
                                      "BootSourceOverrideEnabled": "Once"}}),
            headers={
                'Content-Type': 'application/json',
                'X-Auth-Token': key},
            verify=True
        )
        mock_ilo_logout.assert_called()

    @mock.patch.object(requests, 'get', autospec=True)
    def test_validate_server_profile_template_mac_type_negative(self, mock_get,
                                                                mock__auth):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        server_profile_template_virtual_mac = copy.deepcopy(
            fixtures.SERVER_PROFILE_TEMPLATE_JSON
        )

        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=server_profile_template_virtual_mac
        )
        mock_get.return_value = response

        spt_uuid = utils.get_uuid_from_uri(
            server_profile_template_virtual_mac.get("uri")
        )

        self.assertRaises(
            exceptions.OneViewInconsistentResource,
            oneview_client.validate_server_profile_template_mac_type,
            spt_uuid
        )

    @mock.patch.object(requests, 'get', autospec=True)
    def test_validate_server_profile_template_mac_type(self, mock_get,
                                                       mock__auth):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)

        server_profile_template_physical_mac = (
            fixtures.SERVER_PROFILE_TEMPLATE_LIST_JSON.get("members")[3]
        )

        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=server_profile_template_physical_mac
        )
        mock_get.return_value = response

        spt_uuid = utils.get_uuid_from_uri(
            server_profile_template_physical_mac.get("uri")
        )

        oneview_client.validate_server_profile_template_mac_type(spt_uuid)


@mock.patch.object(client.ClientV2, '_authenticate', autospec=True)
class OneViewClientV2TestCase(unittest.TestCase):

    def setUp(self):
        super(OneViewClientV2TestCase, self).setUp()
        self.manager_url = 'https://1.2.3.4'
        self.username = 'user'
        self.password = 'password'

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_hardware_list(self, mock_get, mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=fixtures.SERVER_HARDWARE_LIST_JSON
        )
        mock_get.return_value = response

        server_hardware_list = oneview_client.server_hardware.list()
        mock_get.assert_called_once_with(
            url='https://1.2.3.4/rest/server-hardware/?start=0&count=9999999',
            headers=mock.ANY,
            verify=True
        )
        for sh in server_hardware_list:
            self.assertIsInstance(sh, models.ServerHardware)

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_hardware_index_list(self, mock_get, mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=fixtures.INDEX_SERVER_HARDWARE_LIST_JSON
        )
        mock_get.return_value = response

        server_hardware_list = oneview_client.server_hardware_index.list()
        mock_get.assert_called_once_with(
            url='https://1.2.3.4/rest/index/resources?' +
                'category=server-hardware&start=0&count=9999999',
            headers=mock.ANY,
            verify=True
        )
        for sh in server_hardware_list:
            self.assertIsInstance(sh, models.ServerHardware)

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_hardware_get(self, mock_get, mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=fixtures.SERVER_HARDWARE_JSON
        )
        mock_get.return_value = response

        sh = oneview_client.server_hardware.get('aaaa-bbbb-cccc')
        mock_get.assert_called_once_with(
            url='https://1.2.3.4/rest/server-hardware/aaaa-bbbb-cccc',
            headers=mock.ANY,
            verify=True
        )
        self.assertIsInstance(sh, models.ServerHardware)

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_hardware_index_get(self, mock_get, mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=fixtures.INDEX_SERVER_HARDWARE_JSON
        )
        mock_get.return_value = response

        sh = oneview_client.server_hardware_index.get('aaaa-bbbb-cccc')
        mock_get.assert_called_once_with(
            url='https://1.2.3.4/rest/index/resources?' +
                'category=server-hardware&filter=uuid:aaaa-bbbb-cccc',
            headers=mock.ANY,
            verify=True
        )
        self.assertIsInstance(sh, models.ServerHardware)

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_hardware_get_not_found(self, mock_get, mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        response = mock_get.return_value
        response.status_code = http_client.NOT_FOUND
        mock_get.return_value = response

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client.server_hardware.get,
            'aaaa-bbbb-cccc'
        )

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_hardware_index_get_not_found(self, mock_get,
                                                 mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        response = mock_get.return_value
        response.status_code = http_client.NOT_FOUND
        mock_get.return_value = response

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client.server_hardware_index.get,
            'aaaa-bbbb-cccc'
        )

    def test_server_hardware_create(self, mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        self.assertRaises(
            NotImplementedError,
            oneview_client.server_hardware.create,
            name='something',
            description='somethingelse',
            something=0
        )

    def test_server_hardware_delete(self, mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        self.assertRaises(
            NotImplementedError,
            oneview_client.server_hardware.delete,
            'aaaa-bbbb-cccc'
        )

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_profile_template_list(self, mock_get, mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=fixtures.SERVER_PROFILE_TEMPLATE_LIST_JSON
        )
        mock_get.return_value = response

        server_profile_template_list = (
            oneview_client.server_profile_template.list()
        )
        mock_get.assert_called_once_with(
            url='https://1.2.3.4/rest/server-profile-templates/'
                '?start=0&count=9999999',
            headers=mock.ANY,
            verify=True
        )
        for spt in server_profile_template_list:
            self.assertIsInstance(spt, models.ServerProfileTemplate)

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_profile_template_get(self, mock_get, mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=fixtures.SERVER_PROFILE_TEMPLATE_JSON
        )
        mock_get.return_value = response

        spt = oneview_client.server_profile_template.get('aaaa-bbbb-cccc')
        mock_get.assert_called_once_with(
            url='https://1.2.3.4/rest/server-profile-templates/aaaa-bbbb-cccc',
            headers=mock.ANY,
            verify=True
        )
        self.assertIsInstance(spt, models.ServerProfileTemplate)

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_profile_template_get_not_found(self, mock_get,
                                                   mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        response = mock_get.return_value
        response.status_code = http_client.NOT_FOUND
        mock_get.return_value = response

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client.server_profile_template.get,
            'aaaa-bbbb-cccc'
        )

    def test_server_profile_template_create(self, mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        self.assertRaises(
            NotImplementedError,
            oneview_client.server_profile_template.create,
            name='something',
            description='somethingelse',
            something=0
        )

    def test_server_profile_template_delete(self, mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        self.assertRaises(
            NotImplementedError,
            oneview_client.server_profile_template.delete,
            'aaaa-bbbb-cccc'
        )

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_profile_list(self, mock_get, mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=fixtures.SERVER_PROFILE_LIST_JSON
        )
        mock_get.return_value = response

        server_profile_list = oneview_client.server_profile.list()
        mock_get.assert_called_once_with(
            url='https://1.2.3.4/rest/server-profiles/?start=0&count=9999999',
            headers=mock.ANY,
            verify=True
        )
        for sp in server_profile_list:
            self.assertIsInstance(sp, models.ServerProfile)

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_profile_get(self, mock_get, mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        response = mock_get.return_value
        response.status_code = http_client.OK
        profile_fixture = copy.deepcopy(fixtures.SERVER_PROFILE_JSON)
        response.json = mock.MagicMock(
            return_value=profile_fixture
        )
        mock_get.return_value = response

        sp = oneview_client.server_profile.get('aaaa-bbbb-cccc')
        mock_get.assert_called_once_with(
            url='https://1.2.3.4/rest/server-profiles/aaaa-bbbb-cccc',
            headers=mock.ANY,
            verify=True
        )
        self.assertIsInstance(sp, models.ServerProfile)

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_profile_get_not_found(self, mock_get, mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        response = mock_get.return_value
        response.status_code = http_client.NOT_FOUND
        mock_get.return_value = response

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client.server_profile.get,
            'aaaa-bbbb-cccc'
        )

    def test_server_profile_create(self, mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        self.assertRaises(
            NotImplementedError,
            oneview_client.server_profile.create,
            name='something',
            description='somethingelse',
            something=0
        )

    @mock.patch.object(client.Client, '_wait_for_task_to_complete')
    @mock.patch.object(requests, 'delete', autospec=True)
    def test_server_profile_delete(self,
                                   mock_delete,
                                   mock__wait_for_task,
                                   mock__authenticate):
        oneview_client = client.ClientV2(self.manager_url,
                                         self.username,
                                         self.password)
        response = mock_delete.return_value
        response.status_code = http_client.OK
        oneview_client._wait_for_task_to_complete = mock__wait_for_task

        oneview_client.server_profile.delete('1111-2222-3333')

        mock_delete.assert_called_once_with(
            url='https://1.2.3.4/rest/server-profiles/1111-2222-3333',
            headers=mock.ANY,
            verify=True
        )


if __name__ == '__main__':
    unittest.main()
