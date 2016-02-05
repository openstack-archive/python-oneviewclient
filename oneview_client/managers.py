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


ONEVIEW_POWER_ON = 'On'
ONEVIEW_POWER_OFF = 'Off'


# class OneViewRequestAPI:
#     def __init__(self, manager_url, username, password,
#                  allow_insecure_connections, tls_cacert_file):
#         self.token = None
#         self.manager_url = manager_url
#         self.username = username
#         self.password = password
#         self.tls_cacert_file = tls_cacert_file
#         self.allow_insecure_connections = allow_insecure_connections
#         self.max_retries = 100
#
#     def _get_verify_connection_option(self):
#         verify_status = False
#         user_cacert = self.tls_cacert_file
#         if self.allow_insecure_connections is False:
#             if(user_cacert is None):
#                 verify_status = True
#             else:
#                 verify_status = user_cacert
#         return verify_status
#
#     def _is_token_valid(self):
#         return self.token is not None
#
#     def _try_execute_request(self, url, request_type, body, headers,
#                              verify_status):
#         try:
#             return requests.request(request_type, url, data=json.dumps(body),
#                                     headers=headers, verify=verify_status)
#         except requests.RequestException as ex:
#             LOG.error(_LE("Can't connect to OneView: %s")
#                       % (str(ex.message).split(':')[-1]))
#             LOG.error(("Can't connect to OneView: %s")
#                       % (str(ex.message).split(':')[-1]))
#             raise exception.OneViewConnectionError(
#                 "Can't connect to OneView: %s" % str(ex.message))
#
#     def _new_token(self):
#         LOG.info(
#             _LI("Using OneView credentials specified in configuration file")
#         )
#         url = '%s%s' % (self.manager_url,
#                         oneview_uri.AUTHENTICATION_URL)
#         body = {
#             'password': self.password,
#             'userName': self.username
#         }
#         headers = {'content-type': 'application/json'}
#         verify_status = self._get_verify_connection_option()
#         if verify_status is False:
#             LOG.warn('Using insecure connection')
#         json_response = None
#         repeat = True
#         while repeat:
#             r = self._try_execute_request(url, 'POST', body, headers,
#                                           verify_status)
#             # NOTE: Workaround to fix JsonDecode problems
#             try:
#                 json_response = r.json()
#                 repeat = self._check_request_status(r)
#             except:
#                 repeat = True
#         return json_response.get('sessionID')
#
#     def _update_token(self):
#         if not self._is_token_valid():
#             self.token = self._new_token()
#
#     def _check_request_status(self, response):
#         repeat = False
#         status = response.status_code
#         response_json = response.json()
#         if status in (409,):
#             ignored_conflicts = {'RABBITMQ_CLIENTCERT_CONFLICT'}
#             if (response_json.get('errorCode') in ignored_conflicts):
#                 repeat = False
#             else:
#                 time.sleep(10)
#                 repeat = True
#             LOG.debug("Conflict contacting OneView: ", response_json)
#         elif status in (404, 500):
#             LOG.error(_LE("Error contacting OneView: "), response_json)
#             LOG.error(("Error contacting OneView: "), response_json)
#         elif status not in (200, 202):
#             LOG.warn("Status not recognized:", status, response_json)
#         return repeat
#
#     def prepare_and_do_request(self, uri, body={}, request_type='GET',
#                                api_version='200'):
#         max_retries = self.max_retries
#
#         self._update_token()
#         headers = {
#             'content-type': 'application/json',
#             'X-Api-Version': api_version,
#             'Auth': self.token
#         }
#         url = '%s%s' % (self.manager_url, uri)
#         verify_status = self._get_verify_connection_option()
#
#         json_response = None
#         repeat = True
#         retries = 0
#         while repeat and (retries < max_retries):
#             r = self._try_execute_request(url, request_type, body, headers,
#                                           verify_status)
#             # NOTE: Workaround to fix JsonDecode problems
#             try:
#                 json_response = r.json()
#                 repeat = self._check_request_status(r)
#             except Exception:
#                 repeat = True
#                 retries += 1
#         return json_response


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

    def list(self):
        resource_uri = self.uri_prefix
        resource_json = self.oneview_client._prepare_and_do_request(
            uri=resource_uri
        )

        members = resource_json.get("members")

        return [self.model.from_json(resource) for resource in members]

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

    def create(self, **kwargs):
        raise NotImplementedError("ServerHardware isn't supposed to be "
                                  "created, only imported.")

    def delete(self, uuid):
        raise NotImplementedError("ServerHardware isn't supposed to be "
                                  "deleted, only removed directly on OneView.")


class ServerProfileTemplateManager(OneViewManager):
    model = models.ServerProfileTemplate
    uri_prefix = '/rest/server-profile-templates/'

    def create(self, **kwargs):
        raise NotImplementedError("ServerProfileTemplate isn't supposed to be "
                                  "created, only imported.")

    def delete(self, uuid):
        raise NotImplementedError("ServerProfileTemplate isn't supposed to be "
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
