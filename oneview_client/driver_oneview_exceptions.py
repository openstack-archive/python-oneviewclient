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

from ironic.common import exception
from ironic.common.i18n import _


class OneViewNotAuthorizedException(exception.IronicException):
    message = _("Unauthorized access to OneView. Check credentials in"
                " ironic.conf.")


class OneViewResourceNotFoundError(exception.IronicException):
    message = _("Resource not Found in OneView")


class OneViewServerProfileTemplateError(exception.IronicException):
    message = _("Server Profile Template not found into driver_info")


class OneViewServerProfileCloneError(exception.IronicException):
    message = _("Error cloning server profile")


class OneViewMaxRetriesExceededError(exception.IronicException):
    message = _("Max connection retries to OneView exceeded")


class OneViewBootDeviceInvalidError(exception.IronicException):
    message = _("The device is not valid to setup the boot order")


class OneViewServerProfileAssociatedError(exception.IronicException):
    message = _("There is no Server Profile associated to this Server"
                " Hardware")


class OneViewErrorStateSettingPowerState(exception.IronicException):
    message = _("Get Error State in OneView trying to set power state of "
                "Server Hardware")


class OneViewTaskError(exception.IronicException):
    message = _("The task for this action in OneView returnet an error state")
