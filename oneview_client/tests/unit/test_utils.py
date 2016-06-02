# -*- encoding: utf-8 -*-
#
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
