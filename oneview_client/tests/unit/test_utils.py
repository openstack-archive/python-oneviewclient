# (c) Copyright 2016 Hewlett Packard Enterprise Development LP
# Copyright 2016 Universidade Federal de Campina Grande
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

from oneview_client import exceptions
from oneview_client.tests import fixtures
from oneview_client import utils


class UtilsTestCase(unittest.TestCase):
    def test__is_uuid_valid_with_valid_uuid(self):
        uuid = 'abcdef12-3456-789f-edcb-aabcdef12345'
        self.assertTrue(utils._is_uuid_valid(uuid))

    def test__is_uuid_valid_with_invalid_uuid(self):
        uuid = 'abcdef12-3456-789f-edcb-aabcdef12345?'
        self.assertFalse(utils._is_uuid_valid(uuid))

    def test_get_uuid_from_uri(self):
        expected_uuid = 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'
        uri = '/rest/resource/' + expected_uuid
        self.assertEqual(expected_uuid, utils.get_uuid_from_uri(uri))

    def test_get_uuid_from_uri_as_none(self):
        self.assertEqual(None, utils.get_uuid_from_uri(None))

    def test_get_uri_from_uuid_with_valid_uuid(self):
        prefix = '/rest/resource/'
        uuid = 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa'
        expected_uri = prefix + uuid
        self.assertEqual(expected_uri, utils.get_uri_from_uuid(prefix, uuid))

    def test_get_uri_from_uuid_with_invalid_uuid(self):
        prefix = '/rest/resource/'
        uuid = 'aaaaaaaa-aaaa-aaaa-aaaa-aaaaaaaaaaaa?'
        self.assertEqual(None, utils.get_uri_from_uuid(prefix, uuid))

    def test__get_empty_bootable_ports(self):
        port = fixtures.TestablePort('AA:BB:CC:DD:EE:FF', bootable=False)
        ports = [port]
        with self.assertRaises(exceptions.OneViewInconsistentResource):
            utils.get_bootable_ports(ports, bootable='true')

    def test__get_empty_not_bootable_ports(self):
        port = fixtures.TestablePort('AA:BB:CC:DD:EE:FF', bootable=True)
        ports = [port]
        with self.assertRaises(exceptions.OneViewInconsistentResource):
            utils.get_bootable_ports(ports, bootable='false')

    def test__get_multiple_bootable_ports(self):
        port1 = fixtures.TestablePort('AA:BB:CC:DD:EE:FA', bootable=True)
        port2 = fixtures.TestablePort('AA:BB:CC:DD:EE:FB', bootable=False)
        port3 = fixtures.TestablePort('AA:BB:CC:DD:EE:FC', bootable=True)
        ports = [port1, port2, port3]
        self.assertEqual(
            [port1, port3],
            utils.get_bootable_ports(ports)
        )

    def test__get_multiple_not_bootable_ports(self):
        port1 = fixtures.TestablePort('AA:BB:CC:DD:EE:FA', bootable=False)
        port2 = fixtures.TestablePort('AA:BB:CC:DD:EE:FB', bootable=True)
        port3 = fixtures.TestablePort('AA:BB:CC:DD:EE:FC', bootable=False)
        ports = [port1, port2, port3]
        self.assertEqual(
            [port1, port3],
            utils.get_bootable_ports(ports, bootable='false')
        )

    def test__get_no_pxe_enabled_ports(self):
        port = fixtures.TestablePort('AA:BB:CC:DD:EE:FF', pxe_enabled=False)
        ports = [port]
        with self.assertRaises(exceptions.OneViewInconsistentResource):
            utils.get_ports_with_llc_and_pxe_enabled(ports)

    def test__get_pxe_enabled_ports(self):
        port = fixtures.TestablePort('AA:BB:CC:DD:EE:FF', pxe_enabled=True)
        ports = [port]
        self.assertEqual(
            ports, utils.get_ports_with_llc_and_pxe_enabled(ports)
        )

    def test__get_multiple_pxe_enabled_ports(self):
        port1 = fixtures.TestablePort('AA:BB:CC:DD:EE:FA', pxe_enabled=True)
        port2 = fixtures.TestablePort('AA:BB:CC:DD:EE:FB', pxe_enabled=False)
        port3 = fixtures.TestablePort('AA:BB:CC:DD:EE:FC', pxe_enabled=True)
        ports = [port1, port2, port3]
        self.assertEqual(
            [port1, port3], utils.get_ports_with_llc_and_pxe_enabled(ports)
        )
