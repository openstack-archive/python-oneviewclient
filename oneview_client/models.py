#
# Copyright 2015 Hewlett Packard Development Company, LP
# Copyright 2015 Universidade Federal de Campina Grande
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

from oneview_client import exceptions
import json


class OneViewObject(object):
    """DO NOT INSTANTIATE. THIS IS AN ABSTRACT CLASS."""

    @classmethod
    def from_json(cls, json):
        instance = cls()
        instance.update_from_json(json)
        return instance

    def update_from_json(self, json):
        for attr_key in self.attribute_map:
            attribute_value = json.get(attr_key)
            setattr(self,
                    self.attribute_map.get(attr_key),
                    attribute_value)


class EnclosureGroup(OneViewObject):
    attribute_map = {
        'uri': 'uri',
        'uuid': 'uuid',
        'name': 'name',
        'enclosureTypeUri': 'enclosure_type_uri',
        'status': 'status',
    }


class Enclosure(OneViewObject):
    attribute_map = {
        'uri': 'uri',
        'enclosureTypeUri': 'enclosure_type_uri',
        'enclosureGroupUri': 'enclosure_group_uri',
        'logicalEnclosureUri': 'logical_enclosure_uri',
        'status': 'status',
    }


class ServerHardwareType(OneViewObject):
    attribute_map = {
        'uri': 'uri',
        'uuid': 'uuid',
        'name': 'name',
    }


class ServerHardware(OneViewObject):
    attribute_map = {
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
        'mpHostInfo': 'mp_host_info',
    }

    def _get_connection_port_info(self, mac_address):
        device_slots = self.port_map.get('deviceSlots')
        for device_slot in device_slots:
            physical_ports = device_slot.get('physicalPorts')
            for physical_port in physical_ports:
                virtual_ports = physical_port.get('virtualPorts')
                for virtual_port in virtual_ports:
                    mac = virtual_port.get('mac')
                    if mac == mac_address:
                        info_dict = {
                            'virtual_port_function': virtual_port.get(
                                'portFunction'
                            ),
                            'physical_port_number': physical_port.get(
                                'portNumber'
                            ),
                            'device_slot_port_number': device_slot.get(
                                'slotNumber'
                            ),
                            'device_slot_location': device_slot.get(
                                'location'
                            ),
                        }
                        return info_dict

    def generate_connection_port_for_mac(self, mac_address):
        port_info = self._get_connection_port_info(mac_address)
        return str(port_info.get('device_slot_location')) + " " +\
            str(port_info.get('device_slot_port_number')) + ":" +\
            str(port_info.get('physical_port_number')) + "-" +\
            str(port_info.get('virtual_port_function'))

    def get_mac(self, nic_index=0):
        if self.port_map:
            device = self.port_map.get('deviceSlots')[0]
            physical_port = device.get('physicalPorts')[nic_index]
            return physical_port.get('mac', '').lower()
        else:
            raise exceptions.OneViewException(
                "There is no portMap on the Server Hardware requested. Is "
                "this a DL server?")

    @property
    def cpus(self):
        return (self.processor_count * self.processor_core_count)


class ServerProfileTemplate(OneViewObject):
    attribute_map = {
        'uri': 'uri',
        'uuid': 'uuid',
        'name': 'name',
        'serverHardwareTypeUri': 'server_hardware_type_uri',
        'enclosureGroupUri': 'enclosure_group_uri',
        'connections': 'connections',
        'boot': 'boot',
    }


class ServerProfile(OneViewObject):
    attribute_map = {
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

    def next_connection_id(self):
        maximum_id = 0
        for connection in self.connections:
            conn_id = int(connection.get('id'))
            if conn_id > maximum_id:
                maximum_id = conn_id
        return maximum_id + 1

    def get_connection(self, id):
        for connection in self.connections:
            if int(connection.get('id')) == id:
                return connection

    # def update_connection(self, id, updated_connection):
    #     for connection in self.connections:
    #         if int(connection.get('id')) == id:
    #             return connection

    def add_connection(self, network_uuid, boot_priority, port_id):
        network_uri = "/rest/ethernet-networks/" + network_uuid
        connection = {
            "id": self.next_connection_id(),
            "functionType": "Ethernet",
            "portId": port_id,
            "networkUri": network_uri,
            "boot": {
                "priority": boot_priority
            }
        }
        self.connections.append(connection)
        return connection

    def remove_connection(self, connection_id):
        index_to_remove = -1
        for conn_index in range(len(self.connections)):
            conn_id = int(self.connections[conn_index].get('id'))
            if conn_id == int(connection_id):
                index_to_remove = conn_index
        if index_to_remove > -1:
            self.connections.pop(index_to_remove)

    def update_from_json(self, json_body):
        """Updates an instance of ServerProfile with values parsed from json

        This method differs from the one in OneViewObject since it adds keys in
        the ServerProfile object for values that aren't on attribute_map. This
        is needed because to send the Server Profile back to OneView, we need
        to preserve state and required fields that aren't exploited by
        python-oneviewclient
        """
        for attr_key in json_body.keys():
            attribute_value = json_body.get(attr_key)
            attribute_map_value = self.attribute_map.get(attr_key)
            if attribute_map_value is not None:
                attr_key = attribute_map_value
            setattr(self, attr_key, attribute_value)

    def to_oneview_dict(self):
        server_profile_dict = {}
        for attr_key in self.__dict__.keys():
            attribute_value = getattr(self, str(attr_key))
            camel_case_key = self._oneview_key_for_attr(self.attribute_map,
                                                        attr_key)
            if camel_case_key is not None:
                attr_key = camel_case_key
            server_profile_dict[attr_key] = attribute_value
        return server_profile_dict

    def _oneview_key_for_attr(self, dictionary, value):
        for k, v in dictionary.items():
            if v == value:
                return k


class EthernetNetwork(OneViewObject):
    TAGGED = 'Tagged'
    UNTAGGED = 'Untagged'
    attribute_map = {
        'vlanId': 'vlan_id',
        'purpose': 'purpose',
        'uri': 'uri',
        'name': 'name',
        'smartLink': 'smartLink',
        'privateNetwork': 'privateNetwork',
        'connectionTemplateUri': 'connectionTemplateUri',
        'ethernetNetworkType': 'ethernetNetworkType',
        'type': 'type',
    }

    def to_oneview_dict(self):
        ethernet_network_dict = {}
        for attr_key in self.__dict__.keys():
            attribute_value = getattr(self, str(attr_key))
            camel_case_key = self._oneview_key_for_attr(self.attribute_map,
                                                        attr_key)
            if camel_case_key is not None:
                attr_key = camel_case_key
            ethernet_network_dict[attr_key] = attribute_value
        return ethernet_network_dict

    def _oneview_key_for_attr(self, dictionary, value):
        for k, v in dictionary.items():
            if v == value:
                return k


class UplinkSet(OneViewObject):
    attribute_map = {
        'uri': 'uri',
        'name': 'name',
        'networkUris': 'network_uris',
        'type': 'type',
        'portConfigInfos': 'port_config_infos',
        'networkType': 'network_type',
        'manualLoginRedistributionState': 'manual_login_redistribution_state',
        'logicalInterconnectUri': 'logical_interconnect_uri',
        'connectionMode': 'connection_mode',
        'fcNetworkUris': 'fc_network_uris',
        'ethernetNetworkType': 'ethernet_network_type'
    }

    def add_network(self, network_uri):
        self.network_uris.append(network_uri)

    def to_oneview_dict(self):
        uplink_set_dict = {}
        for attr_key in self.__dict__.keys():
            attribute_value = getattr(self, str(attr_key))
            camel_case_key = self._oneview_key_for_attr(self.attribute_map,
                                                        attr_key)
            if camel_case_key is not None:
                attr_key = camel_case_key
            uplink_set_dict[attr_key] = attribute_value
        return uplink_set_dict

    def _oneview_key_for_attr(self, dictionary, value):
        for k, v in dictionary.items():
            if v == value:
                return k
