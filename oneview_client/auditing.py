# Copyright 2016 Hewlett Packard Enterprise Development LP.
# Copyright 2016 Universidade Federal de Campina Grande
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

import datetime
import json
import requests
import sys

from six.moves import configparser


def read_audit_map_file(audit_cases_file):
    config = configparser.RawConfigParser()
    config.read(audit_cases_file)
    audit_case = config.get('audit', 'case')
    audit_case_methods = config.get('cases', audit_case)
    return audit_case_methods.split(',')


def audit(f):
    def wrapper(self, *args, **kwargs):
        method = f.__name__
        client_instance_id = id(self)
        method_caller = sys._getframe(1).f_code.co_name

        initial_time = datetime.datetime.now().isoformat()
        ret = f(self, *args, **kwargs)
        end_time = datetime.datetime.now().isoformat()

        is_ironic_request = (
            not callable(getattr(self, method_caller, False)) or
            method_caller == '__init__'
        )
        is_oneview_request = isinstance(ret, requests.models.Response)

        if self.audit_enabled and (method in self.audit_case_methods):
            _log(self, method, ret, initial_time, end_time, client_instance_id,
                 is_ironic_request, is_oneview_request)

        return ret
    return wrapper


def _log(cls, method, ret, initial_time, end_time, client_instance_id,
         is_ironic_request, is_oneview_request):
    if not cls.audit_case_methods:
        raise ValueError('Missing audit case methods.')

    if not cls.audit_output_file:
        raise ValueError('Missing audit output file.')

    data = dict(initial_time=initial_time,
                end_time=end_time,
                method=method,
                ret=str(ret),
                client_instance_id=client_instance_id,
                is_ironic_request=is_ironic_request,
                is_oneview_request=is_oneview_request)

    with open(cls.audit_output_file, 'a') as output:
        json.dump(data, output)
        output.write('\n')
