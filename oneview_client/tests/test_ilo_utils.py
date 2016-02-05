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
import unittest

from oneview_client import ilo_utils


class ILOUtilsTestCase(unittest.TestCase):

    @mock.patch.object(requests, "get", autospec=True)
    @mock.patch.object(requests, "delete", autospec=True)
    def test_ilo_logout(self, mock_delete, mock_get):
        host = "my-host"
        key = "asimplekey"
        resource_href = "/rest/v1/sessions/something/123"

        response = mock_get.return_value
        response.status_code = 200
        response.json.return_value = {
            "Type": "Collection.0",
            "Items": [{
                "Oem": {
                    "Hp": {
                        "MySession": True
                    }
                },
                "links": {
                    "self": {
                        "href": resource_href
                    }
                }
            }],
        }
        response2 = mock_delete.return_value
        response2.status_code = 200
        ilo_utils.ilo_logout(host, key)
        mock_delete.assert_called_once_with(
            "https://" + host + resource_href,
            headers={"X-Auth-Token": "asimplekey"},
            verify=False
        )
