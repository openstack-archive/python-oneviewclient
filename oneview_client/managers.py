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


@six.add_metaclass(abc.ABCMeta)
class OneViewIdentityMapManager(OneViewManager):
    identity_map = {}

    def list(self, **kwargs):
        obj_list = super(OneViewIdentityMapManager, self).list()
        self.identity_map = {obj.uuid: obj for obj in obj_list}
        return self.identity_map.items()

    def get(self, uuid):
        if uuid not in self.identity_map.keys():
            obj = super(OneViewIdentityMapManager, self).get(uuid)
            self.identity_map[uuid] = obj

        return self.identity_map.get(uuid)


@six.add_metaclass(abc.ABCMeta)
class OneViewIndexManager(object):

    def __init__(self, oneview_client):
        self.oneview_client = oneview_client

    @abc.abstractproperty
    def model(self):
        pass

    @abc.abstractproperty
    def uri_index(self):
        pass

    def list(self, **kwargs):
        resource_uri = self.uri_index
        resource_json = self.oneview_client._prepare_and_do_request(
            uri=resource_uri
        )

        members = resource_json.get("members")
        resources = [self.model.from_json(resource) for resource in members]

        for k, v in kwargs.items():
            resources = [r for r in resources if getattr(r, k) == v]

        return resources

    def get(self, uuid):
        resource_uri = self.uri_index + '&filter=uuid:' + str(uuid)
        resource_json = self.oneview_client._prepare_and_do_request(
            uri=resource_uri
        )
        members = resource_json.get("members")
        if len(members) == 0:
            message = "OneView Server Hardware resource not found."
            raise exceptions.OneViewResourceNotFoundError(message)

        return self.model.from_json(members[0])


class EnclosureManager(OneViewManager):
    model = models.Enclosure
    uri_prefix = '/rest/enclosures/'

    def create(self, **kwargs):
        raise NotImplementedError("Enclosure isn't supposed to be created.")

    def delete(self, uuid):
        raise NotImplementedError("Enclosure isn't supposed to be deleted.")


class EnclosureGroupManager(OneViewIdentityMapManager):
    model = models.EnclosureGroup
    uri_prefix = '/rest/enclosure-groups/'

    def create(self, **kwargs):
        raise NotImplementedError("EnclosureGroup isn't supposed to be "
                                  "created.")

    def delete(self, uuid):
        raise NotImplementedError("EnclosureGroup isn't supposed to be "
                                  "deleted.")


class ServerHardwareManager(OneViewManager):
    model = models.ServerHardware
    uri_prefix = '/rest/server-hardware/'

    def create(self, **kwargs):
        raise NotImplementedError("ServerHardware isn't supposed to be "
                                  "created.")

    def delete(self, uuid):
        raise NotImplementedError("ServerHardware isn't supposed to be "
                                  "deleted.")


class ServerHardwareIndexManager(OneViewIndexManager):
    model = models.ServerHardware
    uri_index = '/rest/index/resources?category=server-hardware'


class ServerHardwareTypeManager(OneViewIdentityMapManager):
    model = models.ServerHardwareType
    uri_prefix = '/rest/server-hardware-types/'

    def create(self, **kwargs):
        raise NotImplementedError("ServerHardwareType isn't supposed to be "
                                  "created.")

    def delete(self, uuid):
        raise NotImplementedError("ServerHardwareType isn't supposed to be "
                                  "deleted.")


class ServerProfileManager(OneViewManager):
    model = models.ServerProfile
    uri_prefix = '/rest/server-profiles/'

    def create(self, **kwargs):
        raise NotImplementedError("ServerProfile isn't supposed to be "
                                  "created.")

    def delete(self, uuid):
        raise NotImplementedError("ServerProfile isn't supposed to be "
                                  "deleted.")


class ServerProfileTemplateManager(OneViewManager):
    model = models.ServerProfileTemplate
    uri_prefix = '/rest/server-profile-templates/'

    def create(self, **kwargs):
        raise NotImplementedError("ServerProfileTemplate isn't supposed to be "
                                  "created.")

    def delete(self, uuid):
        raise NotImplementedError("ServerProfileTemplate isn't supposed to be "
                                  "deleted.")
