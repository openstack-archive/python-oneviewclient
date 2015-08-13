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


class OneViewConnectionError(Exception):
    message = "Can't connect to OneView"


class OneViewNotAuthorizedException(Exception):
    message = ("Unauthorized access to OneView. Check credentials in"
               " Ironic configuration file")


class OneViewResourceNotFoundError(Exception):
    message = ("Resource not Found in OneView")


class OneViewServerProfileTemplateError(Exception):
    message = ("Server Profile Template not found in the node's driver_info")


class OneViewMaxPollingAttemptsExceededError(Exception):
    message = ("Max polling attempts to OneView exceeded")


class OneViewBootDeviceInvalidError(Exception):
    message = ("The device is not valid to setup the boot order")


class OneViewServerProfileAssociatedError(Exception):
    message = ("There is no Server Profile associated with this Server"
               " Hardware")


class OneViewErrorStateSettingPowerState(Exception):
    message = ("Server Hardware went to Error State when trying to change"
               " power state")


class OneViewTaskError(Exception):
    message = ("The task for this action in OneView returned an error state")


class OneViewInconsistentResource(Exception):
    message = ("There are inconsistent resources between Ironic and OneView's"
               " side")


class OneViewHealthStatusError(Exception):
    message = ("There is a health status issue with an OneView server profile")
