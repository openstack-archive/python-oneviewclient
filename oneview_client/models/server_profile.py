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
