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

import unittest

from oneview_client.models import Enclosure
from oneview_client.models import EnclosureGroup
from oneview_client.models import ServerHardware
from oneview_client.models import ServerHardwareType
from oneview_client.models import ServerProfile
from oneview_client.models import ServerProfileTemplate


class Test(unittest.TestCase):

    def test_enclosuregroup_from_json(self):
        json = {
            'uri': 'http://something.com/1111-2222-3333-4444',
            'enclosureTypeUri': 'something1',
            'status': 'something2',
        }
        eg = EnclosureGroup.from_json(json)
        enclosure_group_attribute_map = {
            'uri': 'uri',
            'enclosureTypeUri': 'enclosure_type_uri',
            'status': 'status',
        }
        self.assertEqual(eg.attribute_map, enclosure_group_attribute_map)
        self.assertEqual(eg.uri, 'http://something.com/1111-2222-3333-4444')
        self.assertEqual(eg.enclosure_type_uri, 'something1')

    def test_enclosure_from_json(self):
        json = {
            'uri': 'http://something.com/1111-2222-3333-4444',
            'enclosureTypeUri': 'something1',
            'enclosureGroupUri': 'something2',
            'logicalEnclosureUri': 'something3',
            'status': 'something4',
        }
        encl = Enclosure.from_json(json)
        enclosure_attribute_map = {
            'uri': 'uri',
            'enclosureTypeUri': 'enclosure_type_uri',
            'enclosureGroupUri': 'enclosure_group_uri',
            'logicalEnclosureUri': 'logical_enclosure_uri',
            'status': 'status',
        }
        self.assertEqual(encl.attribute_map, enclosure_attribute_map)
        self.assertEqual(encl.uri, 'http://something.com/1111-2222-3333-4444')
        self.assertEqual(encl.logical_enclosure_uri, 'something3')

    def test_serverhardwaretype_from_json(self):
        json = {
            'uri': 'http://something.com/1111-2222-3333-4444',
        }
        sht = ServerHardwareType.from_json(json)
        sht_attribute_map = {
            'uri': 'uri',
        }
        self.assertEqual(sht.attribute_map, sht_attribute_map)
        self.assertEqual(sht.uri, 'http://something.com/1111-2222-3333-4444')

    def test_serverhardware_from_json(self):
        json = {
            'uri': 'http://something.com/1111-2222-3333-4444',
            'uuid': '1111-2222-3333-4444',
            'powerState': 'Powered On',
            'serverProfileUri': 'something1',
            'serverHardwareTypeUri': 'something2',
            'serverGroupUri': 'something3',
            'status': 'something4',
            'stateReason': 'something5',
            'locationUri': 'something6',
            'processorCount': 'something7',
            'processorCoreCount': 'something8',
            'memoryMb': 'something9',
            'mpHostInfo': {
                'mpHostName': '172.18.6.18',
                'mpIpAddresses': [{
                    'address': '172.18.6.18',
                    'type': 'Undefined'
                }]
            }
        }
        sh = ServerHardware.from_json(json)
        sh_attribute_map = {
            'uri': 'uri',
            'uuid': 'uuid',
            'powerState': 'power_state',
            'serverProfileUri': 'server_profile_uri',
            'serverHardwareTypeUri': 'server_hardware_type_uri',
            'serverGroupUri': 'enclosure_group_uri',
            'status': 'status',
            'stateReason': 'state_reason',
            'locationUri': 'enclosure_uri',
            'processorCount': 'processor_count',
            'processorCoreCount': 'processor_core_count',
            'memoryMb': 'memory_mb',
            'portMap': 'port_map',
            'mpHostInfo': 'mp_host_info'
        }
        self.assertEqual(sh.attribute_map, sh_attribute_map)
        self.assertEqual(sh.uri, 'http://something.com/1111-2222-3333-4444')
        self.assertEqual(sh.uuid, '1111-2222-3333-4444')
        self.assertEqual(sh.power_state, 'Powered On')
        self.assertEqual(sh.state_reason, 'something5')
        self.assertDictContainsSubset(
            {'mpIpAddresses': [{
                'address': '172.18.6.18',
                'type': 'Undefined'
                }]
             },
            sh.mp_host_info
        )

    def test_serverprofiletemplate_from_json(self):
        json = {
            'uri': 'http://something.com/1111-2222-3333-4444',
            'serverHardwareTypeUri': 'something1',
            'enclosureGroupUri': 'something2',
        }
        spt = ServerProfileTemplate.from_json(json)
        spt_attribute_map = {
            'uri': 'uri',
            'serverHardwareTypeUri': 'server_hardware_type_uri',
            'enclosureGroupUri': 'enclosure_group_uri',
            'boot': 'boot',
            'connections': 'connections',
        }
        self.assertEqual(spt.attribute_map, spt_attribute_map)
        self.assertEqual(spt.uri, 'http://something.com/1111-2222-3333-4444')
        self.assertEqual(spt.enclosure_group_uri, 'something2')

    def test_serverprofile_from_json(self):
        json = {
            'uri': 'http://something.com',
            'serverProfileTemplateUri': 'something',
            'templateCompliance': 'something',
            'serverHardwareUri': 'something',
            'serverHardwareTypeUri': 'something',
            'enclosureGroupUri': 'something',
            'enclosureUri': 'something',
            'status': 'something',
            'connections': 'something',
            'boot': 'something',
            'sanStorage': 'something',
        }
        sp = ServerProfile.from_json(json)
        server_profile_attribute_map = {
            'uri': 'uri',
            'serverProfileTemplateUri': 'server_profile_template_uri',
            'templateCompliance': 'template_compliance',
            'serverHardwareUri': 'server_hardware_uri',
            'serverHardwareTypeUri': 'server_hardware_type_uri',
            'enclosureGroupUri': 'enclosure_group_uri',
            'enclosureUri': 'enclosure_uri',
            'status': 'status',
            'connections': 'connections',
            'boot': 'boot',
            'sanStorage': 'san_storage',
        }
        self.assertEqual(sp.attribute_map, server_profile_attribute_map)
        self.assertEqual(sp.uri, 'http://something.com')
        self.assertEqual(sp.server_profile_template_uri, 'something')

    def test_serverprofile_to_oneview_dict(self):
        profile = ServerProfile()
        profile.uri = 'http://somehting.com/111-222-333-444'
        self.assertEqual(profile.to_oneview_dict(),
                         {'uri': 'http://somehting.com/111-222-333-444'})

    def test_is_there_any_primary_conn_without_conn(self):
        server_profile = ServerProfile()
        server_profile.connections = []
        self.assertFalse(
            server_profile.is_there_any_primary_connection()
        )

    def test_is_there_any_primary_conn_with_prima_conn(self):
        server_profile = ServerProfile()
        server_profile.connections = [{'boot': {'priority': 'Primary'}}]
        self.assertTrue(
            server_profile.is_there_any_primary_connection()
        )

    def test_is_there_any_prima_conn_without_prim_conn(self):
        server_profile = ServerProfile()
        server_profile.connections = [{'boot': {'priority': 'Secondary'}}]
        self.assertFalse(
            server_profile.is_there_any_primary_connection()
        )

    def test_is_first_port_id_used_without_ports(self):
        server_profile = ServerProfile()
        server_profile.connections = []
        self.assertFalse(server_profile.is_port_id_used('Flb 1:1-a'))

    def test_is_all_port_id_used_with_all_ports_used(self):
        server_profile = ServerProfile()
        server_profile.connections = [
            {'portId': 'Flb 1:1-a'}, {'portId': 'Flb 1:2-a'}
        ]
        self.assertTrue(server_profile.is_port_id_used('Flb 1:1-a'))
        self.assertTrue(server_profile.is_port_id_used('Flb 1:2-a'))

    def check_next_available_port_id(
        self, connections, expected_result
    ):
        server_profile = ServerProfile()
        server_profile.connections = connections
        self.assertEqual(
            expected_result, server_profile.get_next_available_port_id()
        )

    def test_get_next_available_port_id_with_empty_connections(self):
        connections = []
        self.check_next_available_port_id(
            connections=connections,
            expected_result='Flb 1:1-a'
        )

    def test_get_next_available_port_id_with_first_port_used(self):
        connections = [{'portId': 'Flb 1:1-a'}]
        self.check_next_available_port_id(
            connections=connections,
            expected_result='Flb 1:2-a'
        )

    def test_get_next_available_port_id_with_all_ports_used(self):
        connections = [{'portId': 'Flb 1:1-a'}, {'portId': 'Flb 1:2-a'}]
        self.check_next_available_port_id(
            connections=connections,
            expected_result=None
        )
