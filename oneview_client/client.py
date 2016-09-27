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

import abc
import json
import six
import time

import requests
import retrying

from oneview_client import auditing
from oneview_client import exceptions
from oneview_client import ilo_utils
from oneview_client import managers
from oneview_client import states
from oneview_client import utils

SUPPORTED_ONEVIEW_VERSION = 200

WAIT_DO_REQUEST_IN_MILLISECONDS = 1000
WAIT_TASK_IN_MILLISECONDS = 1000

GET_REQUEST_TYPE = 'GET'
PUT_REQUEST_TYPE = 'PUT'
POST_REQUEST_TYPE = 'POST'
DELETE_REQUEST_TYPE = 'DELETE'

MOMENTARY_PRESS = 'MomentaryPress'
PRESS_AND_HOLD = 'PressAndHold'

SERVER_HARDWARE_PREFIX_URI = '/rest/server-hardware/'
SERVER_PROFILE_TEMPLATE_PREFIX_URI = '/rest/server-profile-templates/'
SERVER_PROFILE_PREFIX_URI = '/rest/server-profiles/'


@six.add_metaclass(abc.ABCMeta)
class BaseClient(object):
    def __init__(
            self, manager_url, username, password,
            allow_insecure_connections=False, tls_cacert_file='',
            max_polling_attempts=20, audit_enabled=False,
            audit_map_file='', audit_output_file=''
    ):
        self.manager_url = manager_url
        self.username = username
        self.password = password
        self.allow_insecure_connections = allow_insecure_connections
        self.tls_cacert_file = tls_cacert_file
        self.max_polling_attempts = max_polling_attempts
        self.audit_enabled = audit_enabled
        self.audit_map_file = audit_map_file
        self.audit_output_file = audit_output_file
        self.audit_case_methods = []

        if self.allow_insecure_connections:
            requests.packages.urllib3.disable_warnings(
                requests.packages.urllib3.exceptions.InsecureRequestWarning
            )

        if self.audit_enabled:
            self.audit_case_methods = auditing.read_audit_map_file(
                self.audit_map_file
            )

        self.session_id = self.get_session()

    @auditing.audit
    def verify_credentials(self):
        return self._authenticate()

    @auditing.audit
    def get_session(self):
        response = self._authenticate()
        return response.json().get('sessionID')

    @auditing.audit
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

    @auditing.audit
    def _logout(self):
        if self.manager_url in ("", None):
            raise exceptions.OneViewConnectionError(
                "Can't connect to OneView: 'manager_url' configuration"
                "parameter is blank")

        url = '%s/rest/login-sessions' % self.manager_url
        headers = {
            'X-Api-Version': str(SUPPORTED_ONEVIEW_VERSION),
            'Auth': self.session_id
        }

        verify_ssl = self._get_verify_connection_option()

        r = requests.delete(url,
                            headers=headers,
                            verify=verify_ssl)
        if r.status_code == 400:
            raise exceptions.OneViewNotAuthorizedException()

    @auditing.audit
    def _get_verify_connection_option(self):
        verify_status = False
        user_cacert = self.tls_cacert_file

        if self.allow_insecure_connections is False:
            if not user_cacert:
                verify_status = True
            else:
                verify_status = user_cacert
        return verify_status

    @auditing.audit
    def verify_oneview_version(self):
        if not self._is_oneview_version_compatible():
            msg = ("The version of the OneView's API is unsupported. "
                   "Supported version is '%s'" % SUPPORTED_ONEVIEW_VERSION)
            raise exceptions.IncompatibleOneViewAPIVersion(msg)

    @auditing.audit
    def _is_oneview_version_compatible(self):
        versions = self.get_oneview_version()
        v = SUPPORTED_ONEVIEW_VERSION
        min_version_compatible = versions.get("minimumVersion") <= v
        max_version_compatible = versions.get("currentVersion") >= v
        return min_version_compatible and max_version_compatible

    @auditing.audit
    def get_oneview_version(self):
        url = '%s/rest/version' % self.manager_url
        headers = {"Accept-Language": "en_US"}

        verify_ssl = self._get_verify_connection_option()

        response = requests.get(
            url, headers=headers, verify=verify_ssl
        )
        self._check_request_status(response, url)
        versions = response.json()
        return versions

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
                'X-Api-Version': str(SUPPORTED_ONEVIEW_VERSION),
                'Auth': self.session_id
            }
            url = '%s%s' % (self.manager_url, uri)
            body = json.dumps(body)
            try:
                response = self._do_request(url, headers, body, request_type)
            except exceptions.OneViewNotAuthorizedException:
                self.session_id = self.get_session()
                headers['Auth'] = self.session_id
                response = self._do_request(url, headers, body, request_type)

            json_response = response.json()
        except requests.RequestException as e:
            connection_error = str(e.message).split(':')[-1]
            log_message = ("Can't connect to OneView: %s" % connection_error)
            raise exceptions.OneViewConnectionError(log_message)

        return json_response

    @auditing.audit
    def _do_request(self, url, headers, body, request_type):
        verify_status = self._get_verify_connection_option()

        @retrying.retry(
            stop_max_attempt_number=self.max_polling_attempts,
            retry_on_result=lambda response: self._check_request_status(
                response, url
            ),
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

    @auditing.audit
    def _wait_for_task_to_complete(self, task):
        @retrying.retry(
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

    @auditing.audit
    def _get_ilo_access(self, server_hardware_uuid):
        uri = ("/rest/server-hardware/%s/remoteConsoleUrl"
               % server_hardware_uuid)
        json = self._prepare_and_do_request(uri)
        url = json.get("remoteConsoleUrl")
        ip_key = "addr="
        host_ip = url[url.rfind(ip_key) + len(ip_key):]
        host_ip = host_ip[:host_ip.find("&")]
        session_key = "sessionkey="
        token = url[url.rfind(session_key) + len(session_key):]

        return host_ip, token

    @auditing.audit
    def get_sh_mac_from_ilo(self, server_hardware_uuid, nic_index=0):
        host_ip, ilo_token = self._get_ilo_access(server_hardware_uuid)
        try:
            return ilo_utils.get_mac_from_ilo(host_ip, ilo_token, nic_index)
        finally:
            ilo_utils.ilo_logout(host_ip, ilo_token)

    @auditing.audit
    def _set_onetime_boot(self, server_hardware_uuid, boot_device):
        host_ip, ilo_token = self._get_ilo_access(server_hardware_uuid)
        oneview_ilo_mapping = {
            'HardDisk': 'Hdd',
            'PXE': 'Pxe',
            'CD': 'Cd',
            'USB': 'Usb',
        }
        try:
            ilo_device = oneview_ilo_mapping[boot_device]
            return ilo_utils.set_onetime_boot(host_ip, ilo_token,
                                              ilo_device,
                                              self.allow_insecure_connections)
        except exceptions.IloException as e:
            raise e
        except KeyError as e:
            raise exceptions.IloException(
                "Set one-time boot to %s is not supported." % boot_device
            )
        finally:
            ilo_utils.ilo_logout(host_ip, ilo_token)

    def _check_request_status(self, response, url):
        repeat = False
        status = response.status_code

        if status in (401, 403):
            error_code = response.json().get('errorCode')
            raise exceptions.OneViewNotAuthorizedException(error_code)
        elif status == 404:
            raise exceptions.OneViewResourceNotFoundError(url)
        elif status in (408, 409,):
            time.sleep(10)
            repeat = True
        elif status == 500:
            raise exceptions.OneViewInternalServerError()
        # Any other unexpected status are logged
        elif status not in (200, 202,):
            message = (
                "OneView appliance returned an unknown response status: %s"
                % status
            )
            raise exceptions.UnknowOneViewResponseError(message)
        return repeat


class ClientV2(BaseClient):
    def __init__(
            self, manager_url, username, password,
            allow_insecure_connections=False, tls_cacert_file='',
            max_polling_attempts=20, audit_enabled=False,
            audit_map_file='', audit_output_file=''
    ):
        super(ClientV2, self).__init__(manager_url, username, password,
                                       allow_insecure_connections,
                                       tls_cacert_file, max_polling_attempts,
                                       audit_enabled, audit_map_file,
                                       audit_output_file)

        # Next generation
        self.enclosure = managers.EnclosureManager(self)
        self.enclosure_group = managers.EnclosureGroupManager(self)
        self.server_hardware = managers.ServerHardwareManager(self)
        self.server_hardware_index = managers.ServerHardwareIndexManager(self)
        self.server_hardware_type = managers.ServerHardwareTypeManager(self)
        self.server_profile = managers.ServerProfileManager(self)
        self.server_profile_template = managers.ServerProfileTemplateManager(
            self
        )


class Client(BaseClient):
    def __init__(
            self, manager_url, username, password,
            allow_insecure_connections=False, tls_cacert_file='',
            max_polling_attempts=20, audit_enabled=False,
            audit_map_file='', audit_output_file=''
    ):
        super(Client, self).__init__(manager_url, username, password,
                                     allow_insecure_connections,
                                     tls_cacert_file, max_polling_attempts,
                                     audit_enabled, audit_map_file,
                                     audit_output_file)
        # Next generation
        self._enclosure_group = managers.EnclosureGroupManager(self)
        self._server_hardware = managers.ServerHardwareManager(self)
        self._server_profile_template = managers.ServerProfileTemplateManager(
            self
        )
        self._server_profile = managers.ServerProfileManager(self)

    # --- Power Driver ---
    @auditing.audit
    def get_node_power_state(self, node_info):
        return self.get_server_hardware(node_info).power_state

    @auditing.audit
    def power_on(self, node_info):
        if self.get_node_power_state(node_info) == states.ONEVIEW_POWER_ON:
            ret = states.ONEVIEW_POWER_ON
        else:
            ret = self.set_node_power_state(node_info, states.ONEVIEW_POWER_ON)
        return ret

    @auditing.audit
    def power_off(self, node_info):
        if self.get_node_power_state(node_info) == states.ONEVIEW_POWER_OFF:
            ret = states.ONEVIEW_POWER_OFF
        else:
            ret = self.set_node_power_state(
                node_info, states.ONEVIEW_POWER_OFF, PRESS_AND_HOLD
            )
        return ret

    @auditing.audit
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

        return state

    # --- Management Driver ---
    @auditing.audit
    def get_server_hardware(self, node_info):
        uuid = node_info['server_hardware_uri'].split("/")[-1]
        return self._server_hardware.get(uuid)

    @auditing.audit
    def get_server_hardware_by_uuid(self, uuid):
        return self._server_hardware.get(uuid)

    @auditing.audit
    def get_server_profile_from_hardware(self, node_info):
        server_hardware = self.get_server_hardware(node_info)
        server_profile_uri = server_hardware.server_profile_uri

        if server_profile_uri is None:
            message = (
                "There is no server profile assigned to"
                " %(server_hardware_uri)s" %
                {'server_hardware_uri': node_info.get('server_hardware_uri')}
            )
            raise exceptions.OneViewServerProfileAssociatedError(message)

        server_profile_uuid = server_profile_uri.split("/")[-1]
        return self._server_profile.get(server_profile_uuid)

    @auditing.audit
    def get_server_profile_template(self, node_info):
        uuid = node_info['server_profile_template_uri'].split("/")[-1]
        return self._server_profile_template.get(uuid)

    @auditing.audit
    def get_server_profile_template_by_uuid(self, uuid):
        return self._server_profile_template.get(uuid)

    @auditing.audit
    def get_server_profile_by_uuid(self, uuid):
        return self._server_profile.get(uuid)

    @auditing.audit
    def get_boot_order(self, node_info):
        server_profile = self.get_server_profile_from_hardware(
            node_info
        )
        return server_profile.boot.get("order")

    @auditing.audit
    def set_boot_device(self, node_info, new_primary_boot_device,
                        onetime=False):
        if new_primary_boot_device is None:
            raise exceptions.OneViewBootDeviceInvalidError()

        boot_order = self.get_boot_order(node_info)
        if new_primary_boot_device == boot_order[0]:
            return

        if onetime:
            try:
                sh_uuid = utils.get_uuid_from_uri(
                    node_info['server_hardware_uri']
                )
                self._set_onetime_boot(sh_uuid, new_primary_boot_device)
                return
            except exceptions.IloException:
                # Falls back to persistent in case of failure
                pass

        self._persistent_set_boot_device(node_info, boot_order,
                                         new_primary_boot_device)

    @auditing.audit
    def _persistent_set_boot_device(self, node_info, boot_order,
                                    new_primary_boot_device):

        if new_primary_boot_device in boot_order:
            boot_order.remove(new_primary_boot_device)

        boot_order.insert(0, new_primary_boot_device)

        server_profile = self.get_server_profile_from_hardware(
            node_info
        )

        manage_boot = server_profile.boot.get("manageBoot")
        server_profile.boot = {
            "manageBoot": manage_boot,
            "order": boot_order
        }

        boot_order_dict = server_profile.to_oneview_dict()

        task = self._prepare_and_do_request(
            uri=server_profile.uri, body=boot_order_dict,
            request_type=PUT_REQUEST_TYPE
        )
        try:
            self._wait_for_task_to_complete(task)
        except exceptions.OneViewTaskError as e:
            raise exceptions.OneViewErrorSettingBootDevice(e.message)

    # ---- Deploy Driver ----
    @auditing.audit
    def clone_template_and_apply(self,
                                 server_profile_name,
                                 server_hardware_uuid,
                                 server_profile_template_uuid):

        if not server_profile_name:
            raise ValueError(
                'Missing Server Profile name.'
            )

        if not server_hardware_uuid:
            raise ValueError(
                'Missing Server Hardware uuid.'
            )

        if not server_profile_template_uuid:
            raise ValueError(
                'Missing Server Profile Template uuid.'
            )

        server_hardware_uri = '%s%s' % (
            SERVER_HARDWARE_PREFIX_URI,
            server_hardware_uuid
        )

        server_profile_template_uri = '%s%s' % (
            SERVER_PROFILE_TEMPLATE_PREFIX_URI,
            server_profile_template_uuid
        )

        generate_new_profile_uri = '%s/new-profile' % (
            server_profile_template_uri
        )

        server_profile_from_template_json = self._prepare_and_do_request(
            uri=generate_new_profile_uri
        )

        server_profile_from_template_json['serverHardwareUri'] = (
            server_hardware_uri
        )
        server_profile_from_template_json['name'] = server_profile_name
        server_profile_from_template_json['serverProfileTemplateUri'] = ""

        post_profile_task = self._prepare_and_do_request(
            uri=SERVER_PROFILE_PREFIX_URI,
            body=server_profile_from_template_json,
            request_type=POST_REQUEST_TYPE
        )

        try:
            complete_task = self._wait_for_task_to_complete(
                post_profile_task
            )
        except exceptions.OneViewTaskError as e:
            raise exceptions.OneViewServerProfileAssignmentError(e.message)

        server_profile_uri = (
            complete_task.get('associatedResource').get('resourceUri')
        )

        uuid = server_profile_uri.split("/")[-1]
        server_profile = self.get_server_profile_by_uuid(uuid)

        return server_profile

    @auditing.audit
    def delete_server_profile(self, uuid):
        if not uuid:
            raise ValueError('Missing Server Profile uuid.')

        delete_profile_task = self._prepare_and_do_request(
            uri='%s%s' % (SERVER_PROFILE_PREFIX_URI, uuid),
            request_type=DELETE_REQUEST_TYPE
        )
        try:
            complete_task = self._wait_for_task_to_complete(
                delete_profile_task
            )
        except exceptions.OneViewTaskError as e:
            raise exceptions.OneViewServerProfileDeletionError(e.message)

        return complete_task.get('associatedResource').get('resourceUri')

    # ---- Node Validate ----
    @auditing.audit
    def validate_node_server_hardware(
            self, node_info, node_memorymb, node_cpus
    ):
        node_sh_uri = node_info.get('server_hardware_uri')
        server_hardware = self.get_server_hardware(node_info)
        if str(server_hardware.memory_mb) != str(node_memorymb):
            message = (
                "Node memory_mb is inconsistent with OneView's"
                " server hardware %(server_hardware_uri)s memoryMb."
                % {'server_hardware_uri': node_sh_uri}
            )
            raise exceptions.OneViewInconsistentResource(message)

    @auditing.audit
    def validate_node_server_hardware_type(self, node_info):
        node_sht_uri = node_info.get('server_hardware_type_uri')
        server_hardware = self.get_server_hardware(node_info)
        server_hardware_sht_uri = server_hardware.server_hardware_type_uri

        if server_hardware_sht_uri != node_sht_uri:
            message = (
                "Node server_hardware_type_uri is inconsistent"
                " with OneView's server hardware %(server_hardware_uri)s"
                " serverHardwareTypeUri." %
                {'server_hardware_uri': node_info.get('server_hardware_uri')}
            )
            raise exceptions.OneViewInconsistentResource(message)

    @auditing.audit
    def check_server_profile_is_applied(self, node_info):
        self.get_server_profile_from_hardware(node_info)

    @auditing.audit
    def validate_node_enclosure_group(self, node_info):
        server_hardware = self.get_server_hardware(node_info)
        sh_enclosure_group_uri = server_hardware.enclosure_group_uri
        node_enclosure_group_uri = node_info.get('enclosure_group_uri')

        if node_enclosure_group_uri not in ('', 'None', None):
            if sh_enclosure_group_uri != node_enclosure_group_uri:
                message = (
                    "Node enclosure_group_uri '%(node_enclosure_group_uri)s' "
                    "is inconsistent with OneView's server hardware "
                    "serverGroupUri '%(sh_enclosure_group_uri)s' of "
                    "ServerHardware %(server_hardware)s"
                    % {
                        'node_enclosure_group_uri': node_enclosure_group_uri,
                        'sh_enclosure_group_uri': sh_enclosure_group_uri,
                        'server_hardware': server_hardware.uuid,
                    }
                )
                raise exceptions.OneViewInconsistentResource(message)

    @auditing.audit
    def is_node_port_mac_compatible_with_server_profile(
            self, node_info, ports
    ):
        server_profile = self.get_server_profile_from_hardware(
            node_info
        )

        if server_profile.connections:
            primary_boot_connection = None

            for connection in server_profile.connections:
                boot = connection.get('boot')
                if (boot is not None and
                        boot.get('priority').lower() == 'primary'):
                    primary_boot_connection = connection

            if primary_boot_connection is None:
                message = (
                    "No primary boot connection configured for server profile"
                    " %s." % server_profile.uri
                )
                raise exceptions.OneViewInconsistentResource(message)

            mac = primary_boot_connection.get('mac')

        else:
            # If no connections on Server Profile, the connections are not
            # being managed or the server is rack based. In both cases, fall
            # back to 1st nic from iLO
            server_hardware = self.get_server_hardware(node_info)
            mac = self.get_sh_mac_from_ilo(server_hardware.uuid, nic_index=0)

        is_mac_address_compatible = True
        for port in ports:
            port_address = port.__dict__.get('_obj_address')
            if port_address is None:
                port_address = port.__dict__.get('_address')
            if port_address.lower() != mac.lower():
                is_mac_address_compatible = False

        if (not is_mac_address_compatible) or len(ports) == 0:
            message = (
                "The ports of the node are not compatible with its"
                " server profile %(server_profile_uri)s." %
                {'server_profile_uri': server_profile.uri}
            )
            raise exceptions.OneViewInconsistentResource(message)

    @auditing.audit
    def is_node_port_mac_compatible_with_server_hardware(
            self, node_info, ports
    ):
        server_hardware = self.get_server_hardware(node_info)
        try:
            mac = server_hardware.get_mac(nic_index=0)
        except exceptions.OneViewException:
            mac = self.get_sh_mac_from_ilo(server_hardware.uuid, nic_index=0)

        is_mac_address_compatible = True
        for port in ports:
            port_address = port.__dict__.get('_obj_address')
            if port_address is None:
                port_address = port.__dict__.get('_address')

            if port_address.lower() != mac:
                is_mac_address_compatible = False

        if (not is_mac_address_compatible) or len(ports) == 0:
            message = (
                "The ports of the node are not compatible with its"
                " server hardware %(server_hardware_uri)s." %
                {'server_hardware_uri': server_hardware.uri}
            )
            raise exceptions.OneViewInconsistentResource(message)

    @auditing.audit
    def validate_node_server_profile_template(self, node_info):
        server_profile_template = self.get_server_profile_template(node_info)
        server_hardware = self.get_server_hardware(node_info)

        self._validate_spt_server_hardware_type(
            server_profile_template, server_hardware
        )
        self._validate_spt_enclosure_group(
            server_profile_template, server_hardware
        )
        self._validate_spt_manage_boot(server_profile_template)

    @auditing.audit
    def _validate_spt_server_hardware_type(
        self, server_profile_template, server_hardware
    ):
        spt_server_hardware_type_uri = (
            server_profile_template.server_hardware_type_uri
        )
        sh_server_hardware_type_uri = server_hardware.server_hardware_type_uri

        if spt_server_hardware_type_uri != sh_server_hardware_type_uri:
            message = (
                "Server profile template %(spt_uri)s serverHardwareTypeUri is"
                " inconsistent with server hardware %(server_hardware_uri)s"
                " serverHardwareTypeUri." %
                {'spt_uri': server_profile_template.uri,
                 'server_hardware_uri': server_hardware.uri}
            )
            raise exceptions.OneViewInconsistentResource(message)

    @auditing.audit
    def _validate_spt_enclosure_group(
        self, server_profile_template, server_hardware
    ):
        spt_enclosure_group_uri = server_profile_template.enclosure_group_uri
        sh_enclosure_group_uri = server_hardware.enclosure_group_uri

        if spt_enclosure_group_uri != sh_enclosure_group_uri:
            message = (
                "Server profile template %(spt_uri)s enclosureGroupUri is"
                " inconsistent with server hardware %(server_hardware_uri)s"
                " serverGroupUri." %
                {'spt_uri': server_profile_template.uri,
                 'server_hardware_uri': server_hardware.uri}
            )
            raise exceptions.OneViewInconsistentResource(message)

    @auditing.audit
    def _validate_spt_manage_boot(self, server_profile_template):
        manage_boot = server_profile_template.boot.get('manageBoot')

        if not manage_boot:
            message = (
                "Server Profile Template: %s, does not allow to manage "
                "boot order." % server_profile_template.uri
            )
            raise exceptions.OneViewInconsistentResource(message)

    @auditing.audit
    def _validate_spt_boot_connections(self, server_profile_template):
        spt_connections = server_profile_template.connections

        for connection in spt_connections:
            boot = connection.get('boot')
            if boot and boot.get('priority').lower() == 'primary':
                return
        message = (
            "No primary boot connection configured for server profile"
            " template %s." % server_profile_template.uri
        )
        raise exceptions.OneViewInconsistentResource(message)

    @auditing.audit
    def validate_server_profile_template_mac_type(self, uuid):
        server_profile_template = self.get_server_profile_template_by_uuid(
            uuid
        )

        if server_profile_template.mac_type != 'Physical':
            message = (
                "The server profile template %s is not set to use"
                " physical MAC." % server_profile_template.uri
            )
            raise exceptions.OneViewInconsistentResource(message)
