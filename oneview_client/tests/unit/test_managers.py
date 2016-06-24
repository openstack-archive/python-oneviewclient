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
from oneview_client import managers
from oneview_client import models
from oneview_client.tests import fixtures


class TestManagerBase(unittest.TestCase):

    @mock.patch.object(client, "BaseClient", autospec=True)
    def setUp(self, mock_client):
        self.oneview_client = mock_client(
            manager_url='https://something', username='user', password='pass'
        )


class TestServerHardwareManager(TestManagerBase):

    def test_get(self):
        pass


class TestServerHardwareIndexManager(TestManagerBase):

    @mock.patch.object(client, "ClientV2", autospec=True)
    def test_list(self, mock_client):
        self.oneview_client._prepare_and_do_request.return_value = (
            fixtures.INDEX_SERVER_HARDWARE_LIST_JSON
        )
        index_manager = managers.ServerHardwareIndexManager(
            self.oneview_client
        )
        objects = index_manager.list()
        self.oneview_client._prepare_and_do_request.assert_called_once_with(
            uri=managers.ServerHardwareIndexManager.uri_index
        )
        for obj in objects:
            self.assertIsInstance(obj, models.ServerHardware)

    def test_get(self):
        uuid = "37333036-3831-584D-5131-303030323038"
        json = fixtures.INDEX_SERVER_HARDWARE_JSON

        json['members'] = [m for m in json['members']
                           if m.get('uri').endswith(uuid)]

        self.oneview_client._prepare_and_do_request.return_value = json

        index_manager = managers.ServerHardwareIndexManager(
            self.oneview_client
        )
        obj = index_manager.get(uuid)
        self.oneview_client._prepare_and_do_request.assert_called_once_with(
            uri=managers.ServerHardwareIndexManager.uri_index +
            "&filter=uuid:" + uuid
        )
        self.assertIsInstance(obj, models.ServerHardware)
        self.assertEqual(
            obj.uri,
            "/rest/server-hardware/" + uuid
        )


class TestServerProfileManager(TestManagerBase):

    def test_delete(self):
        uuid = 'f2160e28-8107-45f9-b4b2-3119a622a3a1'

        resource_json = self.oneview_client._prepare_and_do_request.\
            return_value
        server_profile_manager = managers.ServerProfileManager(
            self.oneview_client
        )
        server_profile_manager.delete(uuid)

        self.oneview_client._prepare_and_do_request.assert_called_once_with(
            uri=managers.ServerProfileManager.uri_prefix + uuid,
            request_type='DELETE'
        )
        self.oneview_client._wait_for_task_to_complete.assert_called_with(
            resource_json
        )


class TestEthernetNetworkManager(unittest.TestCase):

    @mock.patch.object(client.BaseClient, '_authenticate', autospec=True)
    def setUp(self, mock__authenticate):
        self.oneview_client = client.ClientV2(
            manager_url='https://something', username='user', password='pass')
        self.ethernet_network = self.oneview_client.ethernet_network

    def _test__is_a_valid_ethernet_network_type_expecting_value_with_type(
        self, expected_value, ethernet_network_type
    ):
        self.assertEqual(
            expected_value,
            self.ethernet_network._is_a_valid_ethernet_network_type(
                ethernet_network_type
            )
        )

    def test__is_a_valid_ethernet_network_type_with_invalid_type(self):
        self._test__is_a_valid_ethernet_network_type_expecting_value_with_type(
            False, "invalid"
        )

    def test__is_a_valid_ethernet_network_type_with_untagged_type(self):
        self._test__is_a_valid_ethernet_network_type_expecting_value_with_type(
            True, "Untagged"
        )

    def test__is_a_valid_ethernet_network_type_with_tagged_type(self):
        self._test__is_a_valid_ethernet_network_type_expecting_value_with_type(
            True, "Tagged"
        )

    def test_create_with_invalid_ethernet_network_type(self):
        kwargs = {
            'ethernet_network_type': 'invalid'
        }
        self.assertRaises(
            ValueError, self.ethernet_network.create, **kwargs
        )

    def test_create_with_untagged_ethernet_network_type_and_vlan(self):
        kwargs = {
            'ethernet_network_type': models.EthernetNetwork.UNTAGGED,
            'vlan': 1
        }
        self.assertRaises(
            ValueError, self.ethernet_network.create, **kwargs
        )

    def test_create_with_tagged_ethernet_network_type_without_vlan(self):
        kwargs = {
            'ethernet_network_type': models.EthernetNetwork.TAGGED,
        }
        self.assertRaises(
            ValueError, self.ethernet_network.create, **kwargs
        )

    @mock.patch.object(requests, 'post')
    def test_create_invalid_ethernet_network(self, mock_post):
        kwargs = {
            'ethernet_network_type': models.EthernetNetwork.UNTAGGED,
            'name': 'fake'
        }

        response = mock_post.return_value
        response.status_code = http_client.BAD_REQUEST
        mock_post.return_value = response

        self.assertRaises(
            exceptions.UnknowOneViewResponseError,
            self.ethernet_network.create, **kwargs
        )

    @mock.patch.object(
        client.BaseClient, '_wait_for_task_to_complete', autospec=True
    )
    @mock.patch.object(
        client.BaseClient, "_prepare_and_do_request", autospec=True
    )
    def test_create_tagged_ethernet_network(
        self, mock__prepare_and_do_request, mock__wait_for_task_to_complete
    ):
        kwargs = {
            'ethernet_network_type': models.EthernetNetwork.TAGGED,
            'vlan': 1,
            'name': 'fake'
        }

        expected_ethernet_network_json = {
            "vlanId": kwargs.get('vlan'),
            "purpose": "General",
            "name": kwargs.get('name'),
            "smartLink": False,
            "privateNetwork": False,
            "connectionTemplateUri": None,
            "ethernetNetworkType": kwargs.get('ethernet_network_type'),
            "type": "ethernet-networkV3",
            "uri": None
        }

        self.ethernet_network.create(**kwargs)
        mock__prepare_and_do_request.assert_called_once_with(
            self.oneview_client,
            uri='/rest/ethernet-networks/',
            body=expected_ethernet_network_json,
            request_type='POST'
        )

    @mock.patch.object(
        client.BaseClient, '_wait_for_task_to_complete', autospec=True
    )
    @mock.patch.object(
        client.BaseClient, "_prepare_and_do_request", autospec=True
    )
    def test_create_untagged_ethernet_network(
        self, mock__prepare_and_do_request, mock__wait_for_task_to_complete
    ):
        kwargs = {
            'ethernet_network_type': models.EthernetNetwork.UNTAGGED,
            'name': 'fake'
        }

        expected_ethernet_network_json = {
            "vlanId": '',
            "purpose": "General",
            "name": kwargs.get('name'),
            "smartLink": False,
            "privateNetwork": False,
            "connectionTemplateUri": None,
            "ethernetNetworkType": kwargs.get('ethernet_network_type'),
            "type": "ethernet-networkV3",
            "uri": None
        }

        self.ethernet_network.create(**kwargs)
        mock__prepare_and_do_request.assert_called_once_with(
            self.oneview_client,
            uri='/rest/ethernet-networks/',
            body=expected_ethernet_network_json,
            request_type='POST'
        )

    @mock.patch.object(
        client.BaseClient, '_wait_for_task_to_complete', autospec=True
    )
    @mock.patch.object(
        client.BaseClient, '_prepare_and_do_request', autospec=True
    )
    @mock.patch.object(managers.EthernetNetworkManager, 'get', autospec=True)
    def test_update_name(
        self, mock_get, mock__prepare_and_do_request,
        mock__wait_for_task_to_complete
    ):
        network_uuid = 'net-uuid'
        network_uri = "/rest/ethernet-networks/" + network_uuid
        new_name = 'new-name'

        original_ethernet_network_json = {
            "uri": network_uri,
            "vlanId": '',
            "purpose": "General",
            "name": 'original_name',
            "smartLink": False,
            "privateNetwork": False,
            "connectionTemplateUri": None,
            "ethernetNetworkType": 'Untagged',
            "type": "ethernet-networkV3"
        }

        network_obj = models.EthernetNetwork.from_json(
            original_ethernet_network_json
        )
        mock_get.return_value = network_obj

        self.ethernet_network.update_name(
            network_uuid, new_name
        )

        expected_network = network_obj
        expected_network.name = new_name
        mock__prepare_and_do_request.assert_called_once_with(
            self.oneview_client, uri=network_uri,
            body=expected_network.to_oneview_dict(),
            request_type='PUT'
        )

    @mock.patch.object(managers.EthernetNetworkManager, 'get', autospec=True)
    def test_update_name_with_nonexistent_ethernet_network(
        self, mock_get
    ):
        network_uuid = 'net-uuid'
        new_name = 'new-name'

        mock_get.return_value = None
        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            self.ethernet_network.update_name,
            network_uuid, new_name
        )

    @mock.patch.object(
        client.BaseClient, '_wait_for_task_to_complete', autospec=True
    )
    @mock.patch.object(
        client.BaseClient, '_prepare_and_do_request', autospec=True
    )
    def test_delete(
        self, mock__prepare_do_request, mock__wait_for_task_to_complete
    ):
        network_uuid = 'abcdef12-3456-789f-edcb-aabcdef12345'
        fake_uri = "/rest/ethernet-networks/" + network_uuid
        self.ethernet_network.delete(network_uuid)
        mock__prepare_do_request.assert_called_once_with(
            self.oneview_client, uri=fake_uri,
            request_type='DELETE'
        )


class TestUplinkSetManager(unittest.TestCase):

    @mock.patch.object(client.BaseClient, '_authenticate', autospec=True)
    def setUp(self, mock__authenticate):
        self.oneview_client = client.ClientV2(
            manager_url='https://something', username='user', password='pass')
        self.uplink_set_manager = self.oneview_client.uplink_set

    @mock.patch.object(managers.UplinkSetManager, 'get', autospec=True)
    def test_add_nonexistent_network(self, mock_get):
        network_uuid = 'net-uuid'
        uplink_set_uuid = 'us-uuid'

        mock_get.return_value = None

        self.assertRaises(
            exceptions.OneViewResourceNotFoundError,
            self.uplink_set_manager.add_network, uplink_set_uuid, network_uuid
        )

    @mock.patch.object(
        client.BaseClient, '_wait_for_task_to_complete', autospec=True
    )
    @mock.patch.object(
        client.BaseClient, '_prepare_and_do_request', autospec=True
    )
    @mock.patch.object(managers.UplinkSetManager, 'get', autospec=True)
    def test_add_network(
        self, mock_get, mock__prepare_and_do_request,
        mock__wait_for_task_to_complete
    ):
        network_uuid = 'net-uuid'
        network_uri = '/rest/ethernet-networks/' + network_uuid
        uplink_set_uuid = 'us-uuid'
        uplink_set = models.UplinkSet()
        uplink_set.uri = '/rest/uplink-sets/' + uplink_set_uuid

        mock_get.return_value = uplink_set

        self.uplink_set_manager.add_network(uplink_set_uuid, network_uuid)

        uplink_set.add_network(network_uri)

        mock__prepare_and_do_request.assert_called_once_with(
            self.oneview_client, uri=uplink_set.uri,
            body=uplink_set.to_oneview_dict(), request_type='PUT'
        )
