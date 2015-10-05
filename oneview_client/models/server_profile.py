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


from oneview_client.models.oneview_object import OneViewObject


class ServerProfile(OneViewObject):

    def __init__(self):
        pass
        self.attribute_map = {
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

    def get_instance_from_json(self, json_body):
        for attr_key in json_body.keys():
            attribute_value = json_body.get(attr_key)
            attribute_map_value = self.attribute_map.get(attr_key)
            if attribute_map_value is not None:
                attr_key = attribute_map_value
            setattr(self, attr_key, attribute_value)
        return self

    def parse_to_oneview_dict(self):
        server_profile_dict = {}
        for attr_key in self.__dict__.keys():
            attribute_value = getattr(self, str(attr_key))
            camel_case_key = self._keys_of_value(self.attribute_map, attr_key)
            if camel_case_key is not None:
                attr_key = camel_case_key
            server_profile_dict[attr_key] = attribute_value
        del server_profile_dict['attribute_map']
        return server_profile_dict

    def _keys_of_value(self, dictionary, value):
        for key in dictionary.keys():
            if dictionary.get(key) == value:
                return key
