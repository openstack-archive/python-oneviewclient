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
from oneview_client import utils


class OneViewObject(object):
    """DO NOT INSTANTIATE. THIS IS AN ABSTRACT CLASS."""

    def __init__(self, json=None):
        self._populate_with_default_values(json)

    def _get_default_value_or_from_json(self, attr_key, json):
        value = None
        if json is None or json.get(attr_key) is None:
            if hasattr(self, 'default_values'):
                value = self.default_values.get(attr_key)
        else:
            value = json.get(attr_key)
        return value

    def _populate_with_default_values(self, json):
        for attr_key in self.attribute_map:
            attribute_value = self._get_default_value_or_from_json(
                attr_key, json
            )
            setattr(self,
                    self.attribute_map.get(attr_key),
                    attribute_value)

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

    def to_oneview_dict(self):
        obj_dict = {}
        for attr_key in self.__dict__.keys():
            attribute_value = getattr(self, str(attr_key))
            oneview_key = utils.get_dictionary_key_with_value(
                self.attribute_map, attr_key
            )
            if oneview_key is not None:
                attr_key = oneview_key
            obj_dict[attr_key] = attribute_value
        return obj_dict


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


class EthernetNetwork(OneViewObject):
    TAGGED = 'Tagged'
    UNTAGGED = 'Untagged'
    attribute_map = {
        'vlanId': 'vlan_id',
        'purpose': 'purpose',
        'uri': 'uri',
        'name': 'name',
        'smartLink': 'smart_link',
        'privateNetwork': 'private_network',
        'connectionTemplateUri': 'connection_template_uri',
        'ethernetNetworkType': 'ethernet_network_type',
        'type': 'type',
    }
    default_values = {
        'purpose': 'General',
        'smartLink': False,
        'privateNetwork': False,
        'type': 'ethernet-networkV3',
    }


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
    default_values = {
        'networkUris': [],
    }

    def add_network(self, network_uri):
        self.network_uris.append(network_uri)
