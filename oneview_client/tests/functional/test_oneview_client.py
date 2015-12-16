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
from oneview_client import models
from oneview_client.tests import fixtures


@mock.patch.object(client.Client, '_authenticate', autospec=True)
class OneViewClientTestCase(unittest.TestCase):

    def setUp(self):
        super(OneViewClientTestCase, self).setUp()
        self.manager_url = 'https://1.2.3.4'
        self.username = 'user'
        self.password = 'password'

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_hardware_list(self, mock_get, mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=fixtures.SERVER_HARDWARE_LIST_JSON
        )
        mock_get.return_value = response

        server_hardware_list = oneview_client._server_hardware.list()
        mock_get.assert_called_once_with(
            url='https://1.2.3.4/rest/server-hardware/',
            headers=mock.ANY,
            verify=True
        )
        for sh in server_hardware_list:
            self.assertIsInstance(sh, models.ServerHardware)

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_hardware_get(self, mock_get, mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=fixtures.SERVER_HARDWARE_JSON
        )
        mock_get.return_value = response

        sh = oneview_client._server_hardware.get('aaaa-bbbb-cccc')
        mock_get.assert_called_once_with(
            url='https://1.2.3.4/rest/server-hardware/aaaa-bbbb-cccc',
            headers=mock.ANY,
            verify=True
        )
        self.assertIsInstance(sh, models.ServerHardware)

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_hardware_get_not_found(self, mock_get, mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        response = mock_get.return_value
        response.status_code = http_client.NOT_FOUND
        mock_get.return_value = response

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client._server_hardware.get,
            'aaaa-bbbb-cccc'
        )

    def test_server_hardware_create(self, mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        self.assertRaises(
            NotImplementedError,
            oneview_client._server_hardware.create,
            name='something',
            description='somethingelse',
            something=0
        )

    def test_server_hardware_delete(self, mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        self.assertRaises(
            NotImplementedError,
            oneview_client._server_hardware.delete,
            'aaaa-bbbb-cccc'
        )

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_profile_template_list(self, mock_get, mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=fixtures.SERVER_PROFILE_TEMPLATE_LIST_JSON
        )
        mock_get.return_value = response

        server_profile_template_list = (
            oneview_client._server_profile_template.list()
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
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=fixtures.SERVER_PROFILE_TEMPLATE_JSON
        )
        mock_get.return_value = response

        spt = oneview_client._server_profile_template.get('aaaa-bbbb-cccc')
        mock_get.assert_called_once_with(
            url='https://1.2.3.4/rest/server-profile-templates/aaaa-bbbb-cccc',
            headers=mock.ANY,
            verify=True
        )
        self.assertIsInstance(spt, models.ServerProfileTemplate)

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_profile_template_get_not_found(self, mock_get,
                                                   mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        response = mock_get.return_value
        response.status_code = http_client.NOT_FOUND
        mock_get.return_value = response

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            oneview_client._server_profile_template.get,
            'aaaa-bbbb-cccc'
        )

    def test_server_profile_template_create(self, mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        self.assertRaises(
            NotImplementedError,
            oneview_client._server_profile_template.create,
            name='something',
            description='somethingelse',
            something=0
        )

    def test_server_profile_template_delete(self, mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        self.assertRaises(
            NotImplementedError,
            oneview_client._server_profile_template.delete,
            'aaaa-bbbb-cccc'
        )

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_profile_list(self, mock_get, mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=fixtures.SERVER_PROFILE_LIST_JSON
        )
        mock_get.return_value = response

        server_profile_list = oneview_client._server_profile.list()
        mock_get.assert_called_once_with(
            url='https://1.2.3.4/rest/server-profiles/',
            headers=mock.ANY,
            verify=True
        )
        for sp in server_profile_list:
            self.assertIsInstance(sp, models.ServerProfile)

    @mock.patch.object(requests, 'get', autospec=True)
    def test_server_profile_get(self, mock_get, mock__authenticate):
        oneview_client = client.Client(self.manager_url,
                                       self.username,
                                       self.password)
        response = mock_get.return_value
        response.status_code = http_client.OK
        response.json = mock.MagicMock(
            return_value=fixtures.SERVER_PROFILE_JSON
        )
        mock_get.return_value = response

        sp = oneview_client._server_profile.get('aaaa-bbbb-cccc')
        mock_get.assert_called_once_with(
            url='https://1.2.3.4/rest/server-profiles/aaaa-bbbb-cccc',
            headers=mock.ANY,
            verify=True
        )
        self.assertIsInstance(sp, models.ServerProfile)

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
