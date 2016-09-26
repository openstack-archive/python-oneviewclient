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


def get_all_macs(server_hardware):
    macs = []
    device_slots = server_hardware.port_map.get('deviceSlots')
    physical_ports = get_physical_ports(device_slots)
    virtual_ports = get_virtual_ports(physical_ports)

    macs.extend(get_physical_macs(physical_ports))
    macs.extend(get_virtual_macs(virtual_ports))
    return set(macs)


def get_physical_ports(device_slots):
    physical_ports = []
    for device_slot in device_slots:
        if device_slot and device_slot.get('physicalPorts'):
            physical_ports.extend(device_slot.get('physicalPorts'))
    return physical_ports


def get_virtual_ports(physical_ports):
    virtual_ports = []
    for physical_port in physical_ports:
        if physical_port and physical_port.get('virtualPorts'):
            virtual_ports.extend(physical_port.get('virtualPorts'))
    return virtual_ports


def get_physical_macs(physical_ports):
    physical_macs = []
    for physical_port in physical_ports:
        if physical_port and physical_port.get('mac'):
            physical_macs.append(physical_port.get('mac').lower())
    return physical_macs


def get_virtual_macs(virtual_ports):
    virtual_macs = []
    for virtual_port in virtual_ports:
        if virtual_port and virtual_port.get('mac'):
            virtual_macs.append(virtual_port.get('mac').lower())
    return virtual_macs
