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


def log(cls, func, ret=None, *args, **kwargs):
    if not cls.audit_case_methods:
        raise ValueError('Missing audit case methods.')

    if not cls.audit_output_file:
        raise ValueError('Missing audit output file.')

    time = datetime.datetime.now().isoformat()
    method = func.__name__ + ':' + str(uuid.uuid4())
    with open(cls.audit_output_file, 'a') as output:
        data = dict(time=time,
                    method=method,
                    args=str(args[1:]),
                    kwargs=str(kwargs),
                    ret=str(ret))
        json.dump(data, output)
        output.write('\n')


def audit(f):
    def wrapper(self, *args, **kwargs):
        if (self.audit_enabled and
           f.__name__ in self.audit_case_methods):
            log(self, f, *args, **kwargs)
        ret = f(self, *args, **kwargs)
        if (self.audit_enabled and
           f.__name__ in self.audit_case_methods):
            log(self, f, ret, *args, **kwargs)
        return ret
    return wrapper
