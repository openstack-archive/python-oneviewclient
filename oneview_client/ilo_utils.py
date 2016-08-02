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

import json
import requests

from oneview_client import exceptions


def rest_op(operation, host, suburi, request_headers, request_body,
            x_auth_token, enforce_SSL=True):

    url = 'https://' + host + suburi

    if request_headers is None:
        request_headers = dict()

    # if X-Auth-Token specified, supply it instead of basic auth
    if x_auth_token is not None:
        request_headers['X-Auth-Token'] = x_auth_token

    if operation == "GET":
        response = requests.get(url, headers=request_headers,
                                verify=enforce_SSL)
        return_value = (response.status_code, response.headers,
                        response.json())
    elif operation == "DELETE":
        response = requests.delete(url, headers=request_headers,
                                   verify=enforce_SSL)
        return_value = (response.status_code, response.headers,
                        response.json())
    elif operation == "PATCH":
        response = requests.patch(url, data=json.dumps(request_body),
                                  headers=request_headers, verify=enforce_SSL)
        return_value = (response.status_code, response.headers,
                        response.json())

    return return_value


# REST GET
def rest_get(host, suburi, request_headers, x_auth_token, enforce_SSL=True):
    return rest_op('GET', host, suburi, request_headers, None, x_auth_token,
                   enforce_SSL=enforce_SSL)
    # NOTE:  be prepared for various HTTP responses including 500, 404, etc.


# REST PATCH
def rest_patch(host, suburi, request_headers, request_body, x_auth_token,
               enforce_SSL=True):
    return rest_op('PATCH', host, suburi, request_headers, request_body,
                   x_auth_token, enforce_SSL=enforce_SSL)
    # NOTE:  be prepared for various HTTP responses including 500, 404, etc.


# REST DELETE
def rest_delete(host, suburi, request_headers, x_auth_token, enforce_SSL=True):
    return rest_op('DELETE', host, suburi, request_headers, None, x_auth_token,
                   enforce_SSL=enforce_SSL)
    # NOTE:  be prepared for various HTTP responses including 500, 404, etc.
    # NOTE:  response may be an ExtendedError or may be empty


# this is a generator that returns collection members
def collection(host, collection_uri, request_headers, x_auth_token,
               enforce_SSL=True):

    # get the collection
    status, headers, thecollection = rest_get(host,
                                              collection_uri,
                                              request_headers,
                                              x_auth_token,
                                              enforce_SSL)

    while status < 300:
        # verify expected type

        # NOTE:  Because of the Redfish standards effort, we have versioned
        # many things at 0 in anticipation of them being ratified for version 1
        # at some point.  So this code makes the (unguarranteed) assumption
        # throughout that version 0 and 1 are both legitimate at this point.
        # Don't write code requiring version 0 as we will bump to version 1 at
        # some point.

        # hint:  don't limit to version 0 here as we will rev to 1.0 at some
        # point hopefully with minimal changes
        assert(get_type(thecollection) == 'Collection.0' or
               get_type(thecollection) == 'Collection.1')

        # if this collection has inline items, return those

        # NOTE:  Collections are very flexible in how the represent members.
        # They can be inline in the collection as members of the 'Items' array,
        # or they may be href links in the links/Members array.  The could
        # actually be both.  Typically, iLO implements the inline (Items) for
        # only when the collection is read only.  We have to render it with the
        # href links when an array contains PATCHable items because its complex
        # to PATCH inline collection members.
        # A client may wish to pass in a boolean flag favoring the href links
        # vs. the Items in case a collection contains both.

        if 'Items' in thecollection:
            # iterate items
            for item in thecollection['Items']:
                # if the item has a self uri pointer, supply that for
                # convenience
                memberuri = None
                if 'links' in item and 'self' in item['links']:
                    memberuri = item['links']['self']['href']

                # Read up on Python generator functions to understand what this
                # does.
                yield 200, None, item, memberuri

        # else walk the member links
        elif 'links' in thecollection and 'Member' in thecollection['links']:

            # iterate members
            for memberuri in thecollection['links']['Member']:
                # for each member return the resource indicated by the member
                # link
                status, headers, member = rest_get(host,
                                                   memberuri['href'],
                                                   request_headers,
                                                   x_auth_token,
                                                   enforce_SSL)

                # Read up on Python generator functions to understand what this
                # does.
                yield status, headers, member, memberuri['href']

        # page forward if there are more pages in the collection
        if 'links' in thecollection and 'NextPage' in thecollection['links']:
            next_page = str(thecollection['links']['NextPage']['page'])
            next_link_uri = collection_uri + '?page=' + next_page
            status, headers, thecollection = rest_get(host,
                                                      next_link_uri,
                                                      request_headers,
                                                      x_auth_token,
                                                      enforce_SSL)

        # else we are finished iterating the collection
        else:
            break

    else:
        raise exceptions.IloException("HTTP %s" % status)


def get_mac_from_ilo(host_ip, x_auth_token, nic_index=0, allow_insecure=False):
    # for each system in the systems collection at /rest/v1/Systems
    ilo_hardware = collection(host_ip, '/rest/v1/Systems', None,
                              x_auth_token, enforce_SSL=not allow_insecure)

    for status, headers, system, member_uri in ilo_hardware:
        # verify expected type
        # hint:  don't limit to version 0 here as we will rev to 1.0 at
        # some point hopefully with minimal changes
        assert(get_type(system) == 'ComputerSystem.0' or
               get_type(system) == 'ComputerSystem.1')

        if 'HostMACAddress' not in system['HostCorrelation']:
            raise exceptions.IloException(
                'NIC resource does not contain "MacAddress" property'
            )
        else:
            # Can have more than a link
            return system['HostCorrelation']['HostMACAddress'][nic_index]


def set_onetime_boot(host_ip, x_auth_token, boot_target, allow_insecure=False):
    # for each system in the systems collection at /rest/v1/Systems
    ilo_hardware = collection(host_ip, '/rest/v1/Systems', None,
                              x_auth_token, enforce_SSL=not allow_insecure)

    for status, headers, system, member_uri in ilo_hardware:
        # verify expected type
        # hint:  don't limit to version 0 here as we will rev to 1.0 at
        # some point hopefully with minimal changes
        assert(get_type(system) == 'ComputerSystem.0' or
               get_type(system) == 'ComputerSystem.1')

        if boot_target not in system["Boot"]["BootSourceOverrideSupported"]:
            raise exceptions.IloException(
                "ERROR: %s is not a supported boot option.\n" % boot_target)
        else:
            body = {"Boot": {"BootSourceOverrideTarget": boot_target,
                             "BootSourceOverrideEnabled": "Once"}
                    }
            headers = {"Content-Type": "application/json"}
            status_code, _, response = rest_patch(host_ip, member_uri, headers,
                                                  body, x_auth_token,
                                                  not allow_insecure)
            if status_code != 200:
                raise exceptions.IloException(response)


def ilo_logout(host_ip, x_auth_token):
    sessions = collection(host_ip, '/rest/v1/sessions', None, x_auth_token,
                          enforce_SSL=False)
    for status, headers, member, member_uri in sessions:
        if member.get('Oem').get('Hp').get('MySession') is True:
            status, headers, member = rest_delete(host_ip, member_uri, None,
                                                  x_auth_token, False)
            if status != 200:
                message = "iLO returned HTTP %s" % status
                raise exceptions.IloException(message)
            return status, member


# return the type of an object (down to the major version, skipping minor, and
# errata)
def get_type(obj):
    typever = obj['Type']
    typesplit = typever.split('.')
    return typesplit[0] + '.' + typesplit[1]
