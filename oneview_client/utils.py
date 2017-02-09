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

import json
import re

from oneview_client import exceptions

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


def get_bootable_ports(ports, bootable):
    bootable_ports = []
    for port in ports:
        switch_info = get_switch_info_from_port(port)
        if switch_info.get('bootable').lower() == str(bootable).lower():
            bootable_ports.append(port)
    return bootable_ports


def get_switch_info_from_port(port):
    local_link_connection = port.local_link_connection
    if not local_link_connection:
        raise exceptions.OneViewInconsistentResource(
            "There must exist a local link connection information on "
            "port for the node."
        )
    switch_info = local_link_connection.get('switch_info')
    if not switch_info:
        raise exceptions.OneViewInconsistentResource(
            "There must exist a switch_info on local link connection "
            "information."
        )
    try:
        switch_info = json.loads(switch_info.replace("'", '"'))
    except Exception:
        raise exceptions.OneViewInconsistentResource(
            "The switch_info information on port is not in a valid format."
        )
    return switch_info


def get_pxe_enabled_ports(ports):
    return [port for port in ports if port.pxe_enabled]
