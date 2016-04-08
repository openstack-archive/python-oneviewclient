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


FIRST_PORT_ID = 'Flb 1:1-a'
SECOND_PORT_ID = 'Flb 1:2-a'

FUNCTION_TYPE_ETHERNET = 'Ethernet'

BOOT_PRIORITY_PRIMARY = 'Primary'


class OneViewObject(object):
    """DO NOT INSTANTIATE. THIS IS AN ABSTRACT CLASS"""

    @classmethod
    def from_json(cls, json):
        instance = cls()
        for attr_key in instance.attribute_map:
            attribute_value = json.get(attr_key)
            setattr(instance,
                    instance.attribute_map.get(attr_key),
                    attribute_value)
        return instance


class EnclosureGroup(OneViewObject):
    attribute_map = {
        'uri': 'uri',
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
    }


class ServerHardware(OneViewObject):
    attribute_map = {
        'uri': 'uri',
        'uuid': 'uuid',
        'powerState': 'power_state',
        'serverProfileUri': 'server_profile_uri',
        'serverHardwareTypeUri': 'server_hardware_type_uri',
        'serverGroupUri': 'enclosure_group_uri',
        'status': 'status',
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
            return physical_port
        else:
            raise exceptions.OneViewException(
                "There is no portMap on the Server Hardware requested. Is "
                "this a DL server?")


class ServerProfileTemplate(OneViewObject):
    attribute_map = {
        'uri': 'uri',
        'serverHardwareTypeUri': 'server_hardware_type_uri',
        'enclosureGroupUri': 'enclosure_group_uri',
        'connections': 'connections',
        'boot': 'boot',
    }


class ServerProfile(OneViewObject):
    attribute_map = {
        'uri': 'uri',
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

    @classmethod
    def from_json(cls, json_body):
        """Returns an instance of ServerProfile with values parsed from json

        This method differs from the one in OneViewObject since it adds keys in
        the ServerProfile object for values that aren't on attribute_map. This
        is needed because to send the Server Profile back to OneView, we need
        to preserve state and required fields that aren't exploited by
        python-oneviewclient
        """
        instance = cls()
        for attr_key in json_body.keys():
            attribute_value = json_body.get(attr_key)
            attribute_map_value = cls.attribute_map.get(attr_key)
            if attribute_map_value is not None:
                attr_key = attribute_map_value
            setattr(instance, attr_key, attribute_value)
        return instance

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

    def is_there_any_primary_connection(self):
        for connection in self.connections:
            boot = connection.get('boot')
            if boot is None:
                continue
            if connection.get('boot').get('priority') == 'Primary':
                return True
        return False

    def is_port_id_used(self, port_id):
        for connection in self.connections:
            if connection.get('portId') == port_id:
                return True
        return False

    def get_next_available_port_id(self):
        if not self.is_port_id_used(FIRST_PORT_ID):
            return FIRST_PORT_ID
        if not self.is_port_id_used(SECOND_PORT_ID):
            return SECOND_PORT_ID
        return None
