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


class OneViewException(Exception):
    message = ("An error occurred in the OneView client.")


class OneViewConnectionError(OneViewException):
    message = ("Can't connect to OneView")


class OneViewNotAuthorizedException(OneViewException):
    message = ("Unauthorized access to OneView. Check the credentials used.")


class OneViewResourceNotFoundError(OneViewException):
    message = ("Resource not found in OneView")


class OneViewServerProfileTemplateError(OneViewException):
    message = ("Server Profile Template not found in the node's driver_info")


class OneViewMaxPollingAttemptsExceededError(OneViewException):
    message = ("Max polling attempts to OneView exceeded")


class OneViewBootDeviceInvalidError(OneViewException):
    message = ("Device selected is not a valid boot device")


class OneViewServerProfileAssociatedError(OneViewException):
    message = ("There is no Server Profile assigned to this Server"
               " Hardware")


class OneViewErrorStateSettingPowerState(OneViewException):
    message = ("Server Hardware went to error state when trying to change"
               " power state")


class OneViewErrorSettingBootDevice(OneViewException):
    message = ("Server Hardware went to error state when trying to change"
               " the primary boot device")


class OneViewTaskError(OneViewException):
    message = ("The task for this action in OneView returned an error state")


class OneViewInconsistentResource(OneViewException):
    message = ("The resource is inconsistent with its OneView counterpart")


class OneViewHealthStatusError(OneViewException):
    message = ("There is a health status issue with an OneView Server Profile")


class IncompatibleOneViewAPIVersion(OneViewException):
    message = ("The version of OneView's API is unsupported")


class UnknowOneViewResponseError(OneViewException):
    message = ("OneView appliance returned an unknown response status")
