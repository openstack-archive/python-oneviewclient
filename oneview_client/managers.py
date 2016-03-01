# -*- encoding: utf-8 -*-
#
# Copyright 2015 Hewlett-Packard Development Company, L.P.
# Copyright 2015 Universidade Federal de Campina Grande
# All Rights Reserved.
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

import abc
import six

from oneview_client import exceptions
from oneview_client import models
from oneview_client import utils


ONEVIEW_POWER_ON = 'On'
ONEVIEW_POWER_OFF = 'Off'


@six.add_metaclass(abc.ABCMeta)
class OneViewManager(object):

    def __init__(self, oneview_client):
        self.oneview_client = oneview_client

    @abc.abstractproperty
    def model(self):
        pass

    @abc.abstractproperty
    def uri_prefix(self):
        pass

    def list(self, **kwargs):
        resource_uri = self.uri_prefix
        resource_json = self.oneview_client._prepare_and_do_request(
            uri=resource_uri
        )

        members = resource_json.get("members")
        resources = [self.model.from_json(resource) for resource in members]

        for k, v in kwargs.items():
            resources = [r for r in resources if getattr(r, k) == v]

        return resources

    def get(self, uuid):
        resource_uri = self.uri_prefix + str(uuid)
        resource_json = self.oneview_client._prepare_and_do_request(
            uri=resource_uri
        )
        if resource_json.get("uri") is None:
            message = "OneView Server Hardware resource not found."
            raise exceptions.OneViewResourceNotFoundError(message)

        return self.model.from_json(resource_json)

    @abc.abstractmethod
    def create(self, **kwargs):
        pass

    @abc.abstractmethod
    def delete(self, uuid):
        pass


class EnclosureManager(OneViewManager):
    model = models.Enclosure
    uri_prefix = '/rest/enclosures/'

    def create(self, **kwargs):
        raise NotImplementedError("Enclosure isn't supposed to be "
                                  "created, only imported.")

    def delete(self, uuid):
        raise NotImplementedError("Enclosure isn't supposed to be "
                                  "deleted, only removed directly on OneView.")


class EnclosureGroupManager(OneViewManager):
    model = models.EnclosureGroup
    uri_prefix = '/rest/enclosure-groups/'

    def create(self, **kwargs):
        raise NotImplementedError("EnclosureGroup isn't supposed to be "
                                  "created, only imported.")

    def delete(self, uuid):
        raise NotImplementedError("EnclosureGroup isn't supposed to be "
                                  "deleted, only removed directly on OneView.")


class ServerHardwareManager(OneViewManager):
    model = models.ServerHardware
    uri_prefix = '/rest/server-hardware/'

    # TODO(thiagop): defer the call to retrieve related objects only when
    # they're called
    def fetch_related_objects(self, sh):
        if sh.enclosure_group_uri:
            eg_uuid = utils.get_uuid_from_uri(sh.enclosure_group_uri)
            eg = EnclosureGroupManager(self.oneview_client).get(eg_uuid)
            sh.enclosure_group = eg

        if sh.server_hardware_type_uri:
            sht_uuid = utils.get_uuid_from_uri(sh.server_hardware_type_uri)
            sht = ServerHardwareTypeManager(self.oneview_client).get(sht_uuid)
            sh.server_hardware_type = sht
        return sh

    def get(self, uuid):
        sh = super(ServerHardwareManager, self).get(self, uuid)
        sh.cpus = sh.processor_count * sh.processor_core_count
        sh = self.fetch_related_objects(sh)
        return sh

    def list(self, **kwargs):
        sh_list = super(ServerHardwareManager, self).list(**kwargs)
        sh_list = [self.fetch_related_objects(sh) for sh in sh_list]
        for sh in sh_list:
            sh.cpus = sh.processor_count * sh.processor_core_count

        return sh_list

    def create(self, **kwargs):
        raise NotImplementedError("ServerHardware isn't supposed to be "
                                  "created, only imported.")

    def delete(self, uuid):
        raise NotImplementedError("ServerHardware isn't supposed to be "
                                  "deleted, only removed directly on OneView.")


class ServerHardwareTypeManager(OneViewManager):
    model = models.ServerHardwareType
    uri_prefix = '/rest/server-hardware-types/'

    def create(self, **kwargs):
        raise NotImplementedError("ServerHardwareType isn't supposed to be "
                                  "created, only imported.")

    def delete(self, uuid):
        raise NotImplementedError("ServerHardwareType isn't supposed to be "
                                  "deleted, only removed directly on OneView.")


class ServerProfileManager(OneViewManager):
    model = models.ServerProfile
    uri_prefix = '/rest/server-profiles/'

    def create(self, **kwargs):
        raise NotImplementedError("ServerProfile isn't supposed to be "
                                  "created, only imported.")

    def delete(self, uuid):
        raise NotImplementedError("ServerProfile isn't supposed to be "
                                  "deleted, only removed directly on OneView.")


class ServerProfileTemplateManager(OneViewManager):
    model = models.ServerProfileTemplate
    uri_prefix = '/rest/server-profile-templates/'

    # TODO(thiagop): defer the call to retrieve related objects only when
    # they're called
    def fetch_related_objects(self, spt):
        if spt.enclosure_group_uri:
            eg_uuid = utils.get_uuid_from_uri(spt.enclosure_group_uri)
            eg = EnclosureGroupManager(self.oneview_client).get(eg_uuid)
            spt.enclosure_group = eg

        if spt.server_hardware_type_uri:
            sht_uuid = utils.get_uuid_from_uri(spt.server_hardware_type_uri)
            sht = ServerHardwareTypeManager(self.oneview_client).get(sht_uuid)
            spt.server_hardware_type = sht
        return spt

    def list(self, **kwargs):
        spt_list = super(ServerProfileTemplateManager, self).list(**kwargs)
        spt_list = [self.fetch_related_objects(spt) for spt in spt_list]
        return spt_list

    def get(self, uuid):
        spt = super(ServerProfileTemplateManager, self).get(uuid)
        spt = self.fetch_related_objects(spt)
        return spt

    def create(self, **kwargs):
        raise NotImplementedError("ServerProfileTemplate isn't supposed to be "
                                  "created, only imported.")

    def delete(self, uuid):
        raise NotImplementedError("ServerProfileTemplate isn't supposed to be "
                                  "deleted, only removed directly on OneView.")
