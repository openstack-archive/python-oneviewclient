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

import json
import os
import time

import requests
import retrying

import states

import driver_oneview_exceptions as exception
from oslo_config import cfg
from oslo_config import types
from oslo_log import log as logging

LOG = logging.getLogger(__name__)

opts = [
    cfg.StrOpt('manager_url',
               help='URL where OneView is available'),
    cfg.StrOpt('username',
               help='OneView username to be used'),
    cfg.StrOpt('password',
               help='OneView password to be used'),
    cfg.StrOpt('nova_username',
               help='Nova username'),
    cfg.StrOpt('nova_user_pass',
               help='Nova password'),
    cfg.StrOpt('nova_user_tenant',
               help='Nova user tenant'),
    cfg.Opt('allow_insecure_connections',
            type=types.Boolean(),
            default=False,
            help='Option to allow insecure connection with OneView'),
    cfg.StrOpt('tls_cacert_file',
               default=None,
               help='Path to CA certificate'),
    cfg.IntOpt('max_retries',
               default=20,
               help='Max connection retries to check changes on OneView'),
]

CONF = cfg.CONF
CONF.register_opts(opts, group='oneview')

ONEVIEW_POWER_ON = 'On'
ONEVIEW_POWER_OFF = 'Off'

SUPPORTED_ONEVIEW_VERSION = 120

POWER_STATE_ONEVIEW_TO_IRONIC = {ONEVIEW_POWER_ON: states.POWER_ON,
                                 ONEVIEW_POWER_OFF: states.POWER_OFF}


def parse_openstack_credentials(os_username, os_password, os_auth_url,
                                os_project_name):
    os_credentials = {
        'os_username': os_username, 'os_password': os_password,
        'os_auth_url': os_auth_url, 'os_tenant_name': os_project_name
    }
    return os_credentials


def check_config_options(func):
    def func_wrapper(*args, **kwargs):
        if not CONF.oneview.manager_url:
            raise Exception("'manager_url' is not provided on [oneview] sect" +
                            "ion of config.")
        elif not CONF.oneview.username:
            raise Exception("'username' is not provided on [oneview] section" +
                            " of config.")
        elif not CONF.oneview.password:
            raise Exception("'password' is not provided on [oneview] section" +
                            " of config.")
        else:
            return func(*args, **kwargs)
    return func_wrapper


def check_request_status(response):
    repeat = False
    status = response.status_code

    if status in (409,):
        LOG.debug("Conflict contacting OneView: ", response.json())
        time.sleep(10)
        repeat = True
    elif status == 404:
        LOG.error("Error contacting OneView: ", response.json())
        raise exception.OneViewResourceNotFoundError()
    elif status == 500:
        LOG.error("Error contacting OneView: ", response.json())
    elif status not in (200, 202):
        LOG.info("Status not recognized:", status, response.json())

    return repeat


def get_verify_connection_option():
    verify_status = False
    user_cacert = CONF.oneview.tls_cacert_file

    if CONF.oneview.allow_insecure_connections is False:
        if user_cacert is None:
            verify_status = True
        else:
            verify_status = user_cacert
    return verify_status


def log_insecure_connection():
    user_cacert = CONF.oneview.tls_cacert_file

    if user_cacert == '':
        LOG.warning("Secure connection to OneView disabled in ironic.conf."
                    " No certificate provided.")
    else:
        if os.path.isfile(user_cacert) is False:
            LOG.warning("Secure connection to OneView disabled in ironic.conf."
                        " Certificate not found.")
        else:
            LOG.info("Secure connection to OneView is disabled in"
                     " ironic.conf. Certificate ignored.")


# --- Authentication ---
@check_config_options
def prepare_and_do_request(uri, body={}, request_type='GET'):
    json_response = {}
    try:
        LOG.info("Using OneView credentials specified in ironic.conf")
        session_token = get_authentication(CONF.oneview.manager_url,
                                           CONF.oneview.username,
                                           CONF.oneview.password)
        if session_token is None:
            raise exception.OneViewNotAuthorizedException()

        headers = {
            'content-type': 'application/json',
            'X-Api-Version': SUPPORTED_ONEVIEW_VERSION,
            'Auth': session_token
        }
        url = '%s%s' % (CONF.oneview.manager_url, uri)
        body = json.dumps(body)

        response = _do_request(url, headers, body, request_type)

        json_response = response.json()
    except requests.RequestException as error_message:
        connection_error = error_message.message
        raise Exception("Can't connect to OneView: %s"
                        % str(connection_error).split(':')[-1])

    return json_response


@retrying.retry(
    stop_max_attempt_number=CONF.oneview.max_retries,
    retry_on_result=lambda response: check_request_status(response),
    wait_fixed=100
)
def _do_request(url, headers, body, request_type):
    verify_status = get_verify_connection_option()

    if request_type == 'PUT':
        response = requests.put(url,
                                data=body,
                                headers=headers,
                                verify=verify_status)
    elif request_type == 'POST':
        response = requests.post(url,
                                 data=body,
                                 headers=headers,
                                 verify=verify_status)
    elif request_type == 'DELETE':
        response = requests.delete(url,
                                   headers=headers,
                                   verify=verify_status)
    else:
        response = requests.get(url,
                                headers=headers,
                                verify=verify_status)

    return response


def _get_authentication_response(manager_url, username, password):
    url = '%s/rest/login-sessions' % manager_url
    body = {'password': password, 'userName': username}
    headers = {'content-type': 'application/json'}

    verify_status = get_verify_connection_option()
    if verify_status is False:
        log_insecure_connection()

    r = requests.post(url,
                      data=json.dumps(body),
                      headers=headers,
                      verify=verify_status)
    return r


def _get_authentication_status_code(manager_url, username, password):
    response = _get_authentication_response(manager_url, username, password)
    return response.status_code


def get_authentication(manager_url, username, password):
    response = _get_authentication_response(manager_url, username, password)
    return response.json().get('sessionID')


def check_oneview_status():
    status_code = None
    try:
        status_code = _get_authentication_status_code(CONF.oneview.manager_url,
                                                      CONF.oneview.username,
                                                      CONF.oneview.password)
    except requests.RequestException as error_message:
        connection_error = error_message.message
        LOG.error("Can't connect to OneView: %s"
                  % (str(connection_error).split(':')[-1]))
        raise NameError("Can't connect to OneView: %s"
                        % str(connection_error).split(':')[-1])

    if status_code is not None:
        if status_code == 200:
            LOG.info("Connection to OneView successfully established.")
        elif status_code == 400:
            LOG.error("Can't connect to OneView: invalid credentials.")
        elif status_code == 408:
            LOG.error("Can't connect to OneView: connection timed out.")
        else:
            LOG.error("Can't connect to OneView. Status Code: %d"
                      % (status_code))


# --- Power Driver ---
def power_on(driver_info):
    if get_node_power_state(driver_info) == states.POWER_ON:
        ret = states.POWER_ON
    else:
        ret = set_node_power_state(driver_info, 'On')
    return ret


def power_off(driver_info):
    if get_node_power_state(driver_info) == states.POWER_OFF:
        ret = states.POWER_OFF
    else:
        ret = set_node_power_state(driver_info, 'Off', 'PressAndHold')
    return ret


def get_node_power_state(driver_info):
    server_hardware_uri = driver_info.get('server_hardware_uri')
    power_state = prepare_and_do_request(uri=server_hardware_uri,
                                         request_type='GET').get('powerState')
    if power_state is None:
        raise exception.OneViewResourceNotFoundError()
    elif power_state == 'On' or power_state == 'PoweringOff':
        return states.POWER_ON
    elif power_state == 'Off' or power_state == 'PoweringOn':
        return states.POWER_OFF
    elif power_state == 'Resetting':
        return states.REBOOT
    else:
        return states.ERROR


def set_node_power_state(driver_info, state, press_type='MomentaryPress'):
    LOG.debug(
        'Setting power state of %(sh_uri)s to %(state)s '
        % {'sh_uri': driver_info.get('server_hardware_uri'),
           'state': state
           }
    )

    body = {'powerState': state, 'powerControl': press_type}
    power_state_uri = driver_info.get('server_hardware_uri') + '/powerState'
    task = prepare_and_do_request(uri=power_state_uri,
                                  body=body,
                                  request_type='PUT')
    try:
        _wait_for_task_to_complete(task)
    except exception.OneViewTaskError as e:
        LOG.error(e.message)
        raise exception.OneViewErrorStateSettingPowerState()

    current_state = get_node_power_state(driver_info)

    if current_state is states.ERROR:
        raise exception.OneViewErrorStateSettingPowerState()

    return get_node_power_state(driver_info)


# --- ManagementDriver ---
def get_server_profile_from_hardware(driver_info):
    server_hardware_json = get_server_hardware(driver_info)
    server_profile_uri = server_hardware_json.get("serverProfileUri")

    if server_profile_uri is None:
        raise exception.OneViewServerProfileAssociatedError()

    server_profile_json = prepare_and_do_request(uri=server_profile_uri)

    if server_profile_json.get("uri") is None:
        raise exception.OneViewResourceNotFoundError()

    return server_profile_json


def get_server_hardware(driver_info):
    server_hardware_json = prepare_and_do_request(
        uri=driver_info.get('server_hardware_uri')
    )
    if server_hardware_json.get("uri") is None:
        raise exception.OneViewResourceNotFoundError()

    return server_hardware_json


def get_boot_order(driver_info):
    server_profile_json = get_server_profile_from_hardware(driver_info)
    return server_profile_json.get("boot").get("order")


def make_boot_order_body(server_profile_dict, order):
    manageBoot = server_profile_dict.get("boot").get("manageBoot")
    server_profile_dict["boot"] = {
        "manageBoot": manageBoot,
        "order": order
    }

    return server_profile_dict


def set_boot_device(driver_info, new_primary_boot_device):
    LOG.info("Setting boot priority to '%s'" % new_primary_boot_device)
    boot_order = get_boot_order(driver_info)

    if new_primary_boot_device is None:
        raise exception.OneViewBootDeviceInvalidError()

    if new_primary_boot_device in boot_order:
        boot_order.remove(new_primary_boot_device)

    boot_order.insert(0, new_primary_boot_device)
    LOG.debug("Boot order now is %s" % str(boot_order))

    server_profile_dict = get_server_profile_from_hardware(driver_info)
    boot_order_body = make_boot_order_body(server_profile_dict, boot_order)

    task = prepare_and_do_request(uri=server_profile_dict.get('uri'),
                                  body=boot_order_body, request_type='PUT')
    _wait_for_task_to_complete(task)
    return


def get_volume_information(uri):
    volume_info_json = prepare_and_do_request(uri)
    if volume_info_json.get("uri") is None:
        raise exception.OneViewResourceNotFoundError()

    return volume_info_json


def _build_clone_body(driver_info, server_profile_dict, server_hardware_dict,
                      server_profile_name):
    server_profile_dict['name'] = server_profile_name
    server_profile_dict['serverHardwareUri'] = server_hardware_dict['uri']

    delete_volume_fields = ['state', 'status']
    delete_fields = ['uuid', 'modified', 'taskUri', 'eTag', 'created',
                     'serialNumber', 'inProgress', 'category', 'state',
                     'enclosureUri', 'associatedServer', 'status',
                     'enclosureBay', 'uri']

    add_volume_fields = []

    volumeAttachments = server_profile_dict["sanStorage"]["volumeAttachments"]
    for storage_information in volumeAttachments:
        volume_data = get_volume_information(storage_information["volumeUri"])
        volume_fields = {"volumeProvisionType": volume_data["provisionType"],
                         "volumeProvisionedCapacityBytes":
                             volume_data["provisionedCapacity"],
                         "volumeShareable": volume_data["shareable"],
                         "volumeName": volume_data["deviceVolumeName"] + "-02",
                         "permanent": volume_data["isPermanent"],
                         "volumeUri": None,
                         "lun": None}
        add_volume_fields.append(volume_fields)

    len_vol_att = len(server_profile_dict["sanStorage"]["volumeAttachments"])
    for i in range(len_vol_att):
        volume_dict = server_profile_dict["sanStorage"]["volumeAttachments"][i]
        volume_dict.update(add_volume_fields[i])

    for i in delete_fields:
        del server_profile_dict[i]

    for j in range(len_vol_att):
        for i in delete_volume_fields:
            del server_profile_dict["sanStorage"]["volumeAttachments"][j][i]

    for j in range(len_vol_att):
        volume = server_profile_dict["sanStorage"]["volumeAttachments"][j]
        storage_paths = volume["storagePaths"]
        for i in range(len(storage_paths)):
            del storage_paths[i]["status"]

    connections_fields = ['id', 'name', 'functionType', 'portId',
                          'requestedMbps', 'networkUri', 'boot']
    fields_to_delete = []

    for j in range(len(server_profile_dict['connections'])):
        for i in server_profile_dict['connections'][j]:
            if not (i in connections_fields):
                if not (i in fields_to_delete):
                    fields_to_delete.append(i)

    for j in range(len(server_profile_dict['connections'])):
        for i in fields_to_delete:
            del server_profile_dict['connections'][j][i]

    return server_profile_dict


def get_server_profile_template(driver_info):
    server_profile_template_uri = (driver_info
                                   .get('server_profile_template_uri'))

    if server_profile_template_uri is None:
        raise exception.OneViewServerProfileTemplateError()

    server_profile_template_json = prepare_and_do_request(
        uri=server_profile_template_uri, request_type='GET'
    )

    if server_profile_template_json.get("uri") is None:
        raise exception.OneViewResourceNotFoundError()

    return server_profile_template_json


def unassign_and_delete(driver_info):
    server_hardware = get_server_hardware(driver_info)
    server_profile_uri = server_hardware.get("serverProfileUri")
    if server_profile_uri:
        LOG.info("Deleting server profile %s",
                 server_hardware.get("serverProfileUri"))
        ret = prepare_and_do_request(uri=server_profile_uri,
                                     request_type="DELETE")
        # TODO(any): check if it really returned a status saying that it'll
        # be deleted
        if not ret:
            LOG.warning("Error deleting server profile: %s."
                        "Consider delete it manually.", ret)
    else:
        LOG.warning("Hardware doesn't have server profile assigned.")


# --- OneView Version---
@check_config_options
def get_oneview_version():
    version_uri = "/rest/version"
    url = '%s%s' % (CONF.oneview.manager_url, version_uri)
    headers = {"Accept-Language": "en_US"}

    verify_status = get_verify_connection_option()
    if verify_status is False:
        log_insecure_connection()

    try:
        versions = requests.get(url, headers=headers,
                                verify=verify_status).json()
    except requests.RequestException as error_message:
        connection_error = error_message.message
        LOG.error("Can't connect to OneView: %s"
                  % (str(connection_error).split(':')[-1]))
        raise NameError("Can't connect to OneView: %s"
                        % str(connection_error).split(':')[-1])

    return versions


def is_oneview_version_compatible():
    versions = get_oneview_version()
    v = SUPPORTED_ONEVIEW_VERSION
    min_version_compatible = versions.get('minimumVersion') <= v
    max_version_compatible = versions.get("currentVersion") >= v

    return min_version_compatible and max_version_compatible


def verify_oneview_version():
    if is_oneview_version_compatible() is True:
        LOG.info("Oneview's REST API version is supported by the OneView "
                 "driver.")
    else:
        LOG.error("OneView's REST API version is NOT supported by the "
                  "OneView driver. The driver's required version is "
                  "%(ov_required_version)i "
                  % {'ov_required_version': SUPPORTED_ONEVIEW_VERSION})


def parse_server_hardware(server_hardware):
    port_map = server_hardware.get('portMap')
    try:
        physical_ports = port_map.get('deviceSlots')[0].get('physicalPorts')
        mac_address = physical_ports[0].get('mac')
    except IndexError:
        raise Exception("Server hardware primary NIC not found.")

    vcpus = (server_hardware["processorCoreCount"] *
             server_hardware["processorCount"])

    return {'name': server_hardware["name"],
            'cpus': vcpus,
            'memory_mb': server_hardware["memoryMb"],
            'local_gb': 500,
            'server_hardware_uri': server_hardware["uri"],
            'server_hardware_type_uri':
                server_hardware["serverHardwareTypeUri"],
            'enclosure_group_uri': server_hardware['serverGroupUri'],
            'cpu_arch': 'x86_64',
            'mac': mac_address
            }


@retrying.retry(
    stop_max_attempt_number=CONF.oneview.max_retries,
    retry_on_result=lambda task: task.get('percentComplete') < 100,
    wait_fixed=1000,
    retry_on_exception=lambda task: False
)
def _wait_for_task_to_complete(task):
    uri = task.get('uri')
    percentComplete = task.get('percentComplete')
    LOG.debug("Waiting for task %s to complete: %s%%" % (uri, percentComplete))
    task = prepare_and_do_request(uri)

    task_state = task.get("taskState")
    error = task.get("errorCode")
    if not task_state and error:
        details = task.get("details")
        if error == "RESOURCE_NOT_FOUND":
            raise exception.OneViewResourceNotFoundError(details)
        else:
            raise exception.OneViewTaskError("%s - %s" % (error, details))
    elif task_state.lower() == 'error':
        raise exception.OneViewTaskError("The task '%s' returned an error"
                                         " state" % uri)
    return task
