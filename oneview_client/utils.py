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
import six

from oslo_serialization import jsonutils

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


def get_oneview_connection_ports(ports):
    llc_pxe_ports = get_ports_with_llc_and_pxe_enabled(ports)
    bootable_ports = get_bootable_ports(llc_pxe_ports)

    return bootable_ports


def get_ports_with_llc_and_pxe_enabled(ports):
    llc_pxe_ports = [port for port in ports if (
        port.local_link_connection and port.pxe_enabled)
    ]
    if not llc_pxe_ports:
        raise exceptions.OneViewInconsistentResource(
            "There must exist at least one port with local link "
            "connection information and pxe_enabled = True at the node."
        )

    return llc_pxe_ports


def get_bootable_ports(ports, bootable='true'):
    bootable_ports = []
    for port in ports:
        switch_info = get_switch_info(port)
        if switch_info and switch_info.get('bootable').lower() == bootable:
            bootable_ports.append(port)

    if not bootable_ports:
        raise exceptions.OneViewInconsistentResource(
            "In the local_link_connection of the port must exist "
            "the switch_info with bootable = true"
        )

    return bootable_ports


def get_switch_info(port):
    switch_info = port.local_link_connection.get('switch_info')
    if switch_info and isinstance(switch_info, six.text_type):
        switch_info = jsonutils.loads(switch_info)

    return switch_info


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
