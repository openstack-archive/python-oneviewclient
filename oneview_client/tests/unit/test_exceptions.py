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

import unittest

from oneview_client import exceptions


class Test(unittest.TestCase):

    def test_create_OneViewException_default_message(self):
        exc = exceptions.OneViewException()
        self.assertEqual(
            str(exc),
            "<%s> %s" % (exc.__class__.__name__, exc.message)
        )

    def test_create_OneViewException_message(self):
        msg = "This is a custom message"
        exc = exceptions.OneViewException(msg)
        self.assertEqual(
            str(exc),
            "<%s> %s" % (exc.__class__.__name__, msg)
        )
