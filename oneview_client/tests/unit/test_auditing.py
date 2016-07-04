# Copyright 2016 Hewlett Packard Enterprise Development LP.
# Copyright 2016 Universidade Federal de Campina Grande
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import mock
import unittest

from oneview_client import auditing
from oneview_client import client

FAKE_AUDITING_METHODS = ['auditable_method']


class OneViewClientAuditTestCase(unittest.TestCase):
    @mock.patch.object(client.ClientV2, '_authenticate', autospec=True)
    def setUp(self, mock__authenticate):
        super(OneViewClientAuditTestCase, self).setUp()
        self.mock_read_audit_map_file = mock.Mock(
            return_value=FAKE_AUDITING_METHODS
        )
        self.mock_log = mock.Mock()
        auditing.read_audit_map_file = self.mock_read_audit_map_file
        auditing._log = self.mock_log

        self.oneview_client = client.ClientV2(
            manager_url='https://1.2.3.4',
            username='username',
            password='password',
            audit_enabled=True,
            audit_map_file='oneview_audit_map_file.conf',
            audit_output_file='oneview_audit_output_file.json'
        )

    @mock.patch.object(client.ClientV2, '_authenticate', autospec=True)
    def test_oneview_auditing_enabled(self, mock__authenticate):
        self.mock_read_audit_map_file.reset_mock()
        self.oneview_client = client.ClientV2(
            manager_url='https://1.2.3.4',
            username='username',
            password='password',
            audit_enabled=True,
            audit_map_file='oneview_audit_map_file.conf',
            audit_output_file='oneview_audit_output_file.json'
        )

        self.assertTrue(self.mock_read_audit_map_file.called)

    @mock.patch.object(client.ClientV2, '_authenticate', autospec=True)
    def test_oneview_auditing_disabled(self, mock__authenticate):
        self.mock_read_audit_map_file.reset_mock()
        self.oneview_client = client.ClientV2(
            manager_url='https://1.2.3.4',
            username='username',
            password='password',
            audit_enabled=False,
            audit_map_file='oneview_audit_map_file.conf',
            audit_output_file='oneview_audit_output_file.json'
        )

        self.assertFalse(self.mock_read_audit_map_file.called)

    def test_oneview_auditing_mapped_method(self):

        class Client(object):
            audit_enabled = True
            audit_output_file = 'oneview_audit_output_file.json'
            audit_case_methods = FAKE_AUDITING_METHODS

            @auditing.audit
            def auditable_method(self):
                pass

        Client().auditable_method()
        self.assertTrue(self.mock_log.called)

    def test_oneview_auditing_not_mapped_method(self):

        class Client(object):
            audit_enabled = True
            audit_output_file = 'oneview_audit_output_file.json'
            audit_case_methods = FAKE_AUDITING_METHODS

            @auditing.audit
            def not_auditable_method(self):
                pass

        Client().not_auditable_method()
        self.assertFalse(self.mock_log.called)
