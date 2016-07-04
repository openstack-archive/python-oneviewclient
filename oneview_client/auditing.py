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
import uuid

from six.moves import configparser


def read_audit_map_file(audit_cases_file):
    config = configparser.RawConfigParser()
    config.read(audit_cases_file)
    audit_case = config.get('audit', 'case')
    audit_case_methods = config.get('cases', audit_case)

    return audit_case_methods.split(',')


def write_audit_output_file(audit_output_file, method_name,
                            args=None, kwargs=None,
                            method_return=None):
    now = datetime.datetime.now().isoformat()

    with open(audit_output_file, "a") as output:
        data = dict(time=now, method_name=method_name)
        if args:
            data['args'] = args
        if kwargs:
            data['kwargs'] = kwargs
        if method_return:
            data['return'] = method_return

        json.dump(data, output)
        output.write('\n')


def audit(f):
    def wrapper(self, *args, **kwargs):

        enabled = self.audit_enabled
        audit_output_file = self.audit_output_file
        audit_case_methods = self.audit_case_methods

        method = f.__name__
        method_name_with_uuid = method + ":" + str(uuid.uuid4())

        if enabled and method in audit_case_methods:
            write_audit_output_file(audit_output_file=audit_output_file,
                                    method_name=method_name_with_uuid,
                                    args=str(args[1:]),
                                    kwargs=str(kwargs))

        method_return = f(self, *args, **kwargs)

        if enabled and method in audit_case_methods:
            write_audit_output_file(audit_output_file=audit_output_file,
                                    method_name=method_name_with_uuid,
                                    method_return=str(method_return))

        return method_return
    return wrapper
