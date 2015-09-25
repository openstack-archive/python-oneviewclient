# -*- encoding: utf-8 -*-
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

import json
import time

import requests
import retrying

from oneview_client import exceptions
from oneview_client import states


SUPPORTED_ONEVIEW_VERSION = 200

WAIT_DO_REQUEST_IN_MILLISECONDS = 100
WAIT_TASK_IN_MILLISECONDS = 1000

GET_REQUEST_TYPE = 'GET'
PUT_REQUEST_TYPE = 'PUT'
POST_REQUEST_TYPE = 'POST'
DELETE_REQUEST_TYPE = 'DELETE'

MOMENTARY_PRESS = 'MomentaryPress'
PRESS_AND_HOLD = 'PressAndHold'


class Client(object):

    def __init__(
        self, manager_url, username, password,
        allow_insecure_connections=False, tls_cacert_file='',
        max_polling_attempts=20
    ):
        self.manager_url = manager_url
        self.username = username
        self.password = password
        self.allow_insecure_connections = allow_insecure_connections
        self.tls_cacert_file = tls_cacert_file
        self.max_polling_attempts = max_polling_attempts

        self.session_id = self.get_session()

    def verify_credentials(self):
        return self._authenticate()

    def get_session(self):
        response = self._authenticate()
        return response.json().get('sessionID')

    def _authenticate(self):
        if self.manager_url in ("", None):
            raise exceptions.OneViewConnectionError(
                "Can't connect to OneView: 'manager_url' configuration"
                "parameter is blank")

        url = '%s/rest/login-sessions' % self.manager_url
        body = {
            'userName': self.username,
            'password': self.password
        }
        headers = {
            'content-type': 'application/json'
        }

        verify_ssl = self._get_verify_connection_option()

        r = requests.post(url,
                          data=json.dumps(body),
                          headers=headers,
                          verify=verify_ssl)

        if r.status_code == 400:
            raise exceptions.OneViewNotAuthorizedException()
        else:
            return r

    def _get_verify_connection_option(self):
        verify_status = False
        user_cacert = self.tls_cacert_file

        if self.allow_insecure_connections is False:
            if not user_cacert:
                verify_status = True
            else:
                verify_status = user_cacert
        return verify_status

    def verify_oneview_version(self):
        if not self._is_oneview_version_compatible():
            raise exceptions.IncompatibleOneViewAPIVersion(
                "The version of the OneView's API is unsupported. Supported "
                "version is '%s'" % SUPPORTED_ONEVIEW_VERSION)

    def _is_oneview_version_compatible(self):
        versions = self.get_oneview_version()
        v = SUPPORTED_ONEVIEW_VERSION
        min_version_compatible = versions.get("minimumVersion") <= v
        max_version_compatible = versions.get("currentVersion") >= v
        return min_version_compatible and max_version_compatible

    def get_oneview_version(self):
        url = '%s/rest/version' % self.manager_url
        headers = {"Accept-Language": "en_US"}

        verify_ssl = self._get_verify_connection_option()

        try:
            versions = requests.get(
                url, headers=headers, verify=verify_ssl
            ).json()
            return versions
        except requests.RequestException as e:
            raise exceptions.OneViewConnectionError(e.message)

    # --- Power Driver ---
    def get_node_power_state(self, node_info):
        server_hardware_json = self.get_server_hardware(node_info)
        power_state = server_hardware_json.get('powerState')

        return power_state

    def power_on(self, node_info):
        if self.get_node_power_state(node_info) == states.ONEVIEW_POWER_ON:
            ret = states.ONEVIEW_POWER_ON
        else:
            ret = self.set_node_power_state(
                node_info, states.ONEVIEW_POWER_ON
            )
        return ret

    def power_off(self, node_info):
        if self.get_node_power_state(node_info) == states.ONEVIEW_POWER_OFF:
            ret = states.ONEVIEW_POWER_OFF
        else:
            ret = self.set_node_power_state(
                node_info, states.ONEVIEW_POWER_OFF, PRESS_AND_HOLD
            )
        return ret

    def set_node_power_state(
        self, node_info, state, press_type=MOMENTARY_PRESS
    ):
        body = {'powerState': state, 'powerControl': press_type}
        power_state_uri = (node_info.get('server_hardware_uri') +
                           '/powerState')
        task = self._prepare_and_do_request(
            uri=power_state_uri, body=body, request_type=PUT_REQUEST_TYPE
        )
        try:
            self._wait_for_task_to_complete(task)
        except exceptions.OneViewTaskError as e:
            raise exceptions.OneViewErrorStateSettingPowerState(e.message)

        current_state = self.get_node_power_state(node_info)

        if current_state is states.ONEVIEW_ERROR:
            message = (
                "Error setting node power state to %(state)s" %
                {"state": state}
            )
            raise exceptions.OneViewErrorStateSettingPowerState(message)

        return current_state

    # --- ManagementDriver ---
    def get_server_hardware(self, node_info):
        server_hardware_uri = node_info.get('server_hardware_uri')
        server_hardware_json = self._prepare_and_do_request(
            uri=server_hardware_uri
        )
        if server_hardware_json.get("uri") is None:
            message = "OneView Server Hardware resource not found."
            raise exceptions.OneViewResourceNotFoundError(message)

        return server_hardware_json

    def get_server_profile_from_hardware(self, node_info):
        server_hardware_json = self.get_server_hardware(node_info)
        server_profile_uri = server_hardware_json.get("serverProfileUri")
        if server_profile_uri is None:
            message = (
                "There is no server profile assigned to"
                " %(server_hardware_uri)s" %
                {'server_hardware_uri': node_info.get('server_hardware_uri')}
            )
            raise exceptions.OneViewServerProfileAssociatedError(message)

        server_profile_json = self._prepare_and_do_request(
            uri=server_profile_uri
        )
        if server_profile_json.get("uri") is None:
            message = "OneView Server Profile resource not found."
            raise exceptions.OneViewResourceNotFoundError(message)

        return server_profile_json

    def get_server_profile_template(self, node_info):
        server_profile_template_uri = (
            node_info.get('server_profile_template_uri')
        )
        server_profile_template_json = self._prepare_and_do_request(
            uri=server_profile_template_uri, request_type=GET_REQUEST_TYPE
        )

        if server_profile_template_json.get("uri") is None:
            message = "OneView Server Profile Template resource not found."
            raise exceptions.OneViewResourceNotFoundError(message)

        return server_profile_template_json

    def get_boot_order(self, node_info):
        server_profile_json = self.get_server_profile_from_hardware(
            node_info
        )
        return server_profile_json.get("boot").get("order")

    def _make_boot_order_body(self, server_profile_dict, order):
        manageBoot = server_profile_dict.get("boot").get("manageBoot")
        server_profile_dict["boot"] = {
            "manageBoot": manageBoot,
            "order": order
        }

        return server_profile_dict

    def set_boot_device(self, node_info, new_primary_boot_device):
        boot_order = self.get_boot_order(node_info)

        if new_primary_boot_device is None:
            raise exceptions.OneViewBootDeviceInvalidError()

        if new_primary_boot_device in boot_order:
            boot_order.remove(new_primary_boot_device)

        boot_order.insert(0, new_primary_boot_device)

        server_profile_dict = self.get_server_profile_from_hardware(
            node_info
        )
        boot_order_body = self._make_boot_order_body(
            server_profile_dict,
            boot_order
        )

        task = self._prepare_and_do_request(
            uri=server_profile_dict.get('uri'), body=boot_order_body,
            request_type=PUT_REQUEST_TYPE
        )
        try:
            self._wait_for_task_to_complete(task)
        except exceptions.OneViewTaskError as e:
            raise exceptions.OneViewErrorSettingBootDevice(e.message)

    # ---- Node validate ----
    def validate_node_server_hardware(
        self, node_info, node_memorymb, node_cpus
    ):
        node_sh_uri = node_info.get('server_hardware_uri')
        server_hardware_json = self.get_server_hardware(node_info)
        server_hardware_memorymb = server_hardware_json.get('memoryMb')
        server_hardware_cpus = (server_hardware_json.get('processorCoreCount')
                                * server_hardware_json.get('processorCount'))
        if server_hardware_memorymb != node_memorymb:
            message = (
                "Node memory_mb is inconsistent with OneView's"
                " server hardware %(server_hardware_uri)s memoryMb."
                % {'server_hardware_uri': node_sh_uri}
            )
            raise exceptions.OneViewInconsistentResource(message)
        elif server_hardware_cpus != node_cpus:
            message = (
                "Node cpus is inconsistent with OneView's"
                " server hardware %(server_hardware_uri)s cpus."
                % {'server_hardware_uri': node_sh_uri}
            )
            raise exceptions.OneViewInconsistentResource(message)

    def validate_node_server_hardware_type(self, node_info):
        node_sht_uri = node_info.get('server_hardware_type_uri')
        server_hardware = self.get_server_hardware(node_info)
        server_hardware_sht_uri = server_hardware.get('serverHardwareTypeUri')

        if server_hardware_sht_uri != node_sht_uri:
            message = (
                "Node server_hardware_type_uri is inconsistent"
                " with OneView's server hardware %(server_hardware_uri)s"
                " serverHardwareTypeUri." %
                {'server_hardware_uri': node_info.get('server_hardware_uri')}
            )
            raise exceptions.OneViewInconsistentResource(message)

    def check_server_profile_is_applied(self, node_info):
        self.get_server_profile_from_hardware(node_info)

    def validate_node_enclosure_group(self, node_info):
        server_hardware = self.get_server_hardware(node_info)
        sh_enclosure_group_uri = server_hardware.get('serverGroupUri')
        node_enclosure_group_uri = node_info.get('enclosure_group_uri')

        if node_enclosure_group_uri is not '':
            if sh_enclosure_group_uri != node_enclosure_group_uri:
                message = (
                    "Node enclosure_group_uri is inconsistent"
                    " with OneView's server hardware %(server_hardware_uri)s"
                    " serverGroupUri." %
                    {'server_hardware_uri': node_info.
                     get('server_hardware_uri')}
                )
                raise exceptions.OneViewInconsistentResource(message)

    def is_node_port_mac_compatible_with_server_profile(
        self, node_info, ports
    ):
        server_profile_json = self.get_server_profile_from_hardware(
            node_info
        )

        primary_boot_connection = None
        for connection in server_profile_json.get('connections'):
            if connection.get('boot').get('priority') == 'Primary':
                primary_boot_connection = connection

        if primary_boot_connection is None:
            message = (
                "No primary boot connection configured for server profile"
                " %s." % server_profile_json.get('uri')
            )
            raise exceptions.OneViewInconsistentResource(message)

        server_profile_mac = primary_boot_connection.get('mac')

        is_mac_address_compatible = True
        for port in ports:
            port_address = port.__dict__.get('_obj_address')
            if port_address is None:
                port_address = port.__dict__.get('_address')
            if port_address.lower() != \
               server_profile_mac.lower():
                is_mac_address_compatible = False

        if (not is_mac_address_compatible) or len(ports) == 0:
            message = (
                "The ports of the node are not compatible with its"
                " server profile %(server_profile_uri)s." %
                {'server_profile_uri': server_profile_json.get('uri')}
            )
            raise exceptions.OneViewInconsistentResource(message)

    def validate_node_server_profile_template(self, node_info):
        node_spt_uri = node_info.get('server_profile_template_uri')

        server_profile_template_json = self.get_server_profile_template(
            node_info
        )
        spt_server_hardware_type_uri = server_profile_template_json \
            .get('serverHardwareTypeUri')
        spt_enclosure_group_uri = server_profile_template_json \
            .get('enclosureGroupUri')

        server_hardware_json = self.get_server_hardware(node_info)
        sh_server_hardware_type_uri = server_hardware_json \
            .get('serverHardwareTypeUri')
        sh_enclosure_group_uri_uri = server_hardware_json \
            .get('serverGroupUri')

        if spt_server_hardware_type_uri != sh_server_hardware_type_uri:
            message = (
                "Server profile template %(spt_uri)s serverHardwareTypeUri is"
                " inconsistent with server hardware %(server_hardware_uri)s"
                " serverHardwareTypeUri." %
                {'spt_uri': node_spt_uri,
                 'server_hardware_uri': node_info.get('server_hardware_uri')}
            )
            raise exceptions.OneViewInconsistentResource(message)
        if spt_enclosure_group_uri != sh_enclosure_group_uri_uri:
            message = (
                "Server profile template %(spt_uri)s enclosureGroupUri is"
                " inconsistent with server hardware %(server_hardware_uri)s"
                " serverGroupUri." %
                {'spt_uri': node_spt_uri,
                 'server_hardware_uri': node_info.get('server_hardware_uri')}
            )
            raise exceptions.OneViewInconsistentResource(message)

    # --- Requests ---
    def _prepare_and_do_request(
        self, uri, body={}, request_type=GET_REQUEST_TYPE
    ):
        json_response = {}
        try:
            if not self.session_id:
                self.session_id = self.get_session()

            headers = {
                'content-type': 'application/json',
                'X-Api-Version': SUPPORTED_ONEVIEW_VERSION,
                'Auth': self.session_id
            }
            url = '%s%s' % (self.manager_url, uri)
            body = json.dumps(body)
            response = self._do_request(url, headers, body, request_type)

            json_response = response.json()
        except requests.RequestException as e:
            connection_error = str(e.message).split(':')[-1]
            log_message = ("Can't connect to OneView: %s" % connection_error)
            raise exceptions.OneViewConnectionError(log_message)

        return json_response

    def _do_request(self, url, headers, body, request_type):
        verify_status = self._get_verify_connection_option()

        @retrying.retry(
            stop_max_attempt_number=self.max_polling_attempts,
            retry_on_result=lambda response: _check_request_status(response),
            wait_fixed=WAIT_DO_REQUEST_IN_MILLISECONDS
        )
        def request(url, headers, body, request_type):

            if request_type == PUT_REQUEST_TYPE:
                response = requests.put(
                    url, data=body, headers=headers, verify=verify_status
                )
            elif request_type == POST_REQUEST_TYPE:
                response = requests.post(
                    url, data=body, headers=headers, verify=verify_status
                )
            elif request_type == DELETE_REQUEST_TYPE:
                response = requests.delete(
                    url, headers=headers, verify=verify_status
                )
            else:
                response = requests.get(
                    url, headers=headers, verify=verify_status
                )
            return response
        return request(url, headers, body, request_type)

    def _wait_for_task_to_complete(self, task):
        @retrying.retry(
            stop_max_attempt_number=self.max_polling_attempts,
            retry_on_result=lambda task: task.get('percentComplete') < 100,
            wait_fixed=WAIT_TASK_IN_MILLISECONDS,
            retry_on_exception=lambda task: False
        )
        def wait(task):
            uri = task.get('uri')
            task = self._prepare_and_do_request(uri)

            task_state = task.get("taskState")
            error_code = task.get("errorCode")
            if (not task_state) and error_code:
                details = task.get("details")
                if error_code == "RESOURCE_NOT_FOUND":
                    raise exceptions.OneViewResourceNotFoundError(details)
                else:
                    raise exceptions.OneViewTaskError("%s - %s"
                                                      % (error_code, details))
            elif task_state.lower() == 'error':
                raise exceptions.OneViewTaskError("The task '%s' returned an "
                                                  "error state" % uri)
            return task
        return wait(task)


def _check_request_status(response):
    repeat = False
    status = response.status_code

    if status == 401:
        raise exceptions.OneViewNotAuthorizedException()
    elif status == 404:
        raise exceptions.OneViewResourceNotFoundError()
    elif status in (409,):
        time.sleep(10)
        repeat = True
    elif status == 500:
        raise exceptions.OneViewInternalServerError(
            "OneView returned HTTP 500"
        )
    # Any other unexpected status are logged
    elif status not in (200, 202,):
        message = (
            "OneView appliance returned an unknown response status: %s"
            % status
        )
        raise exceptions.UnknowOneViewResponseError(message)
    return repeat
