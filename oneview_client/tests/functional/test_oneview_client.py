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
import six.moves.http_client as http_client
import unittest

from oneview_client import client
from oneview_client import exceptions
from oneview_client import ilo_utils
from oneview_client import models
from oneview_client.tests import fixtures
from oneview_client import utils


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
        profile.json = mock.MagicMock(
            return_value=fixtures.SERVER_PROFILE_JSON
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
        profile.json = mock.MagicMock(
            return_value=fixtures.SERVER_PROFILE_JSON
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
    def test_validate_spt_boot_connections(self, mock_get, mock__authenticate):
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
        fails = [
            # Single connection, no primary
            fixtures.SERVER_PROFILE_TEMPLATE_LIST_JSON.get('members')[1],
            # Two connections, any primary
            fixtures.SERVER_PROFILE_TEMPLATE_LIST_JSON.get('members')[4],
            # No connections
            fixtures.SERVER_PROFILE_TEMPLATE_LIST_JSON.get('members')[9],
        ]
        for spt in passes:
            response = mock_get.return_value
            response.status_code = http_client.OK
            response.json = mock.MagicMock(
                return_value=spt
            )
            mock_get.return_value = response
            oneview_client.validate_spt_boot_connections(
                utils.get_uuid_from_uri(spt.get('uri'))
            )
        for spt in fails:
            response = mock_get.return_value
            response.status_code = http_client.OK
            response.json = mock.MagicMock(
                return_value=spt
            )
            mock_get.return_value = response
            self.assertRaises(
                exceptions.OneViewInconsistentResource,
                oneview_client.validate_spt_boot_connections,
                utils.get_uuid_from_uri(spt.get('uri'))
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
        profile.json = mock.MagicMock(
            return_value=fixtures.SERVER_PROFILE_JSON
        )
        mock_get.side_effect = [hardware, profile, hardware, profile]
        oneview_client._wait_for_task_to_complete = mock__wait_for_task

        node_info = {
            'server_hardware_uri':
                '/rest/server-hardware/30303437-3933-4753-4831-31315835524E'
        }

        oneview_client.set_boot_device(node_info, 'PXE')
        mock_put.assert_called_once_with(
            self.manager_url + fixtures.SERVER_PROFILE_JSON.get('uri'),
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
        profile.json = mock.MagicMock(
            return_value=fixtures.SERVER_PROFILE_JSON
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
            data='{"Boot": {"BootSourceOverrideTarget": "Hdd"}}',
            headers={
                'Content-Type': 'application/json',
                'X-Auth-Token': key},
            verify=True
        )
        mock_ilo_logout.assert_called()


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
            url='https://1.2.3.4/rest/server-hardware/',
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
                'category=server-hardware',
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
            url='https://1.2.3.4/rest/server-profile-templates/',
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
            url='https://1.2.3.4/rest/server-profiles/',
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
        response.json = mock.MagicMock(
            return_value=fixtures.SERVER_PROFILE_JSON
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
