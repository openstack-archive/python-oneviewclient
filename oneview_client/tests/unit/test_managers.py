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
import unittest

from oneview_client import client
from oneview_client import managers
from oneview_client import models
from oneview_client.tests import fixtures


class TestServerHardwareManager(unittest.TestCase):

    def test_get(self):
        pass


class TestServerHardwareIndexManager(unittest.TestCase):

    @mock.patch.object(client, "ClientV2", autospec=True)
    def test_list(self, mock_client):
        oneview_client = mock_client(manager_url='https://something',
                                     username='user',
                                     password='pass')
        oneview_client._prepare_and_do_request.return_value = (
            fixtures.INDEX_SERVER_HARDWARE_LIST_JSON
        )
        index_manager = managers.ServerHardwareIndexManager(oneview_client)
        objects = index_manager.list()
        oneview_client._prepare_and_do_request.assert_called_once_with(
            uri=managers.ServerHardwareIndexManager.uri_index + '&start=0'
            '&count=9999999'
        )
        for obj in objects:
            self.assertIsInstance(obj, models.ServerHardware)

    @mock.patch.object(client, "ClientV2", autospec=True)
    def test_get(self, mock_client):
        uuid = "37333036-3831-584D-5131-303030323038"
        oneview_client = mock_client(manager_url='https://something',
                                     username='user',
                                     password='pass')
        json = fixtures.INDEX_SERVER_HARDWARE_JSON

        json['members'] = [m for m in json['members']
                           if m.get('uri').endswith(uuid)]

        oneview_client._prepare_and_do_request.return_value = json

        index_manager = managers.ServerHardwareIndexManager(oneview_client)
        obj = index_manager.get(uuid)
        oneview_client._prepare_and_do_request.assert_called_once_with(
            uri=managers.ServerHardwareIndexManager.uri_index +
            "&filter=uuid:" + uuid
        )
        self.assertIsInstance(obj, models.ServerHardware)
        self.assertEqual(
            obj.uri,
            "/rest/server-hardware/" + uuid
        )


class TestServerProfileManager(unittest.TestCase):

    @mock.patch.object(client, "ClientV2", autospec=True)
    def test_delete(self, mock_client):
        oneview_client = mock_client(manager_url='https://something',
                                     username='user',
                                     password='pass')
        uuid = 'f2160e28-8107-45f9-b4b2-3119a622a3a1'

        resource_json = oneview_client._prepare_and_do_request.return_value
        server_profile_manager = managers.ServerProfileManager(oneview_client)
        server_profile_manager.delete(uuid)

        oneview_client._prepare_and_do_request.assert_called_once_with(
            uri=managers.ServerProfileManager.uri_prefix + uuid,
            request_type='DELETE'
        )
        oneview_client._wait_for_task_to_complete.assert_called_with(
            resource_json
        )
