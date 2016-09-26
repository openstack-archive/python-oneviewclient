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

from oneview_client import models
from oneview_client.tests import fixtures


class Test(unittest.TestCase):

    def test_enclosuregroup_from_json(self):
        json = {
            'uri': 'http://something.com/1111-2222-3333-4444',
            'uuid': '1111-2222-3333-4444',
            'name': 'my-enclosure-group',
            'enclosureTypeUri': 'something1',
            'status': 'something2',
        }
        eg = models.EnclosureGroup.from_json(json)
        enclosure_group_attribute_map = {
            'uri': 'uri',
            'uuid': 'uuid',
            'name': 'name',
            'enclosureTypeUri': 'enclosure_type_uri',
            'status': 'status',
        }
        self.assertEqual(eg.attribute_map, enclosure_group_attribute_map)
        self.assertEqual(eg.uri, 'http://something.com/1111-2222-3333-4444')
        self.assertEqual(eg.uuid, '1111-2222-3333-4444')
        self.assertEqual(eg.name, 'my-enclosure-group')
        self.assertEqual(eg.enclosure_type_uri, 'something1')
        self.assertFalse(hasattr(eg, 'something_not_defined'))

    def test_enclosure_from_json(self):
        json = {
            'uri': 'http://something.com/1111-2222-3333-4444',
            'enclosureTypeUri': 'something1',
            'enclosureGroupUri': 'something2',
            'logicalEnclosureUri': 'something3',
            'status': 'something4',
        }
        encl = models.Enclosure.from_json(json)
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
        self.assertFalse(hasattr(encl, 'something_not_defined'))

    def test_serverhardwaretype_from_json(self):
        json = {
            'uri': 'http://something.com/1111-2222-3333-4444',
            'uuid': 'aaaa-bbbb-cccc',
            'name': 'my-server-hardware-type'
        }
        sht = models.ServerHardwareType.from_json(json)
        sht_attribute_map = {
            'uri': 'uri',
            'uuid': 'uuid',
            'name': 'name'
        }
        self.assertEqual(sht.attribute_map, sht_attribute_map)
        self.assertEqual(sht.uri, 'http://something.com/1111-2222-3333-4444')
        self.assertEqual(sht.uuid, 'aaaa-bbbb-cccc')
        self.assertEqual(sht.name, 'my-server-hardware-type')
        self.assertFalse(hasattr(sht, 'something_not_defined'))

    def test_serverhardware_from_json(self):
        json = {
            'uri': 'http://something.com/1111-2222-3333-4444',
            'uuid': '1111-2222-3333-4444',
            'name': 'my-server-profile',
            'powerState': 'Powered On',
            # NOTE: porpusefully commented to test
            # 'serverProfileUri': 'something1',
            'serverHardwareTypeUri': 'something2',
            'serverGroupUri': 'something3',
            'status': 'something4',
            'state': 'something5',
            'stateReason': 'something6',
            'locationUri': 'something7',
            'processorCount': 'something8',
            'processorCoreCount': 'something9',
            'memoryMb': 'something10',
            'mpHostInfo': {
                'mpHostName': '172.18.6.18',
                'mpIpAddresses': [{
                    'address': '172.18.6.18',
                    'type': 'Undefined'
                }]
            }
        }
        sh = models.ServerHardware.from_json(json)
        sh_attribute_map = {
            'uri': 'uri',
            'uuid': 'uuid',
            'name': 'name',
            'powerState': 'power_state',
            'serverProfileUri': 'server_profile_uri',
            'serverHardwareTypeUri': 'server_hardware_type_uri',
            'serverGroupUri': 'enclosure_group_uri',
            'status': 'status',
            'state': 'state',
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
        self.assertEqual(sh.name, 'my-server-profile')
        self.assertEqual(sh.power_state, 'Powered On')
        self.assertEqual(sh.state, 'something5')
        self.assertEqual(sh.state_reason, 'something6')
        self.assertIsNone(sh.server_profile_uri)
        self.assertFalse(hasattr(sh, 'something_not_defined'))
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
            'name': 'my-server-profile-template',
            'serverHardwareTypeUri': 'something1',
            'enclosureGroupUri': 'something2',
        }
        spt = models.ServerProfileTemplate.from_json(json)
        spt_attribute_map = {
            'uri': 'uri',
            'uuid': 'uuid',
            'name': 'name',
            'serverHardwareTypeUri': 'server_hardware_type_uri',
            'enclosureGroupUri': 'enclosure_group_uri',
            'boot': 'boot',
            'connections': 'connections',
            'macType': 'mac_type',
        }
        self.assertEqual(spt.attribute_map, spt_attribute_map)
        self.assertEqual(spt.uri, 'http://something.com/1111-2222-3333-4444')
        self.assertEqual(spt.enclosure_group_uri, 'something2')
        self.assertFalse(hasattr(spt, 'something_not_defined'))

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
        sp = models.ServerProfile.from_json(json)
        server_profile_attribute_map = {
            'uri': 'uri',
            'name': 'name',
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
        self.assertFalse(hasattr(sp, 'something_not_defined'))

    def test_serverprofile_to_oneview_dict(self):
        profile = models.ServerProfile()
        profile.uri = 'http://somehting.com/111-222-333-444'
        self.assertEqual(profile.to_oneview_dict(),
                         {'uri': 'http://somehting.com/111-222-333-444'})

    def test_get_mac_from_server_hardware(self):
        server_hardware = models.ServerHardware()
        server_hardware.port_map = fixtures.PORT_MAP
        self.assertEqual("d8:9d:67:73:54:00", server_hardware.get_mac())

if __name__ == '__main__':
    unittest.main()
