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

import re

UUID_PATTERN = "^[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-" +\
    "[0-9a-fA-F]{4}-[0-9a-fA-F]{12}$"


def _is_uuid_valid(uuid):
    if re.match(UUID_PATTERN, uuid):
        return True
    return False


def get_uuid_from_uri(uri):
    if uri:
        return uri.split("/")[-1]


def get_uri_from_uuid(resource_prefix, uuid):
    if uuid and _is_uuid_valid(uuid):
        return str(resource_prefix) + str(uuid)
