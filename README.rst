====================
python-oneviewclient
====================

Library to use HPE OneView to provide nodes for Ironic

This library adds a communication layer between Ironic and OneView and
abstracts the version of OneView in place.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/python-oneviewclient
* Source: http://git.openstack.org/cgit/openstack/python-oneviewclient
* Bugs: http://bugs.launchpad.net/python-oneviewclient

Features
========

Audit logging
-------------

The ``python-oneviewclient`` is capable of audit logging calls made from it
to OneView. Currently, data about requests time, methods' name, methods'
parameters and methods' returns, can be recorded to be used in the auditing
process to discover and better understand hostspots, bottle neck and measure
about the performance of the Ironic and OneView integration ecosystem.

Enabling audit logging
""""""""""""""""""""""

For enabling audit logging, a configuration will be necessary and for doing
that the user needs to set three parameters in the configuration of the tool
or driver that will be audit logged. The parameters are: ``audit_enabled``,
``audit_map_file`` and ``audit_output_file``. The ``audit_enabled`` parameter
is for enable/disable the audit logging, while the ``audit_map_file`` and
``audit_output_file`` must to be filled with the absolute path to the audit
map file and the audit output file.

The audit map file
""""""""""""""""""

The audit map file is composed by two sections, ``audit`` and ``cases``. In
``audit`` section there is a ``case`` option where one, and just one, of the
audit logging ``cases`` needs to be specified. And ``cases`` section, needs to
be filled with a name for a cases followed by thoses methods that user wants
to audit logging. The methods that are allowed for the audit logging are those
decorated by ``@auditing.audit`` in ``python-oneviewclient``.

See an example of the audit map file::

    [audit]

    # Case to be audit logged from those declared in cases section.

    case = case_number_one

    [cases]

    # Possible auditable case name followed by the audit loggable
    # methods' names.

    case_number_one = first_method,second_method,third_method
    case_number_two = first_method,third_method,fifth_method


The audit output file
"""""""""""""""""""""

The result of the audit logging process is a json file that can be used by
auditors, operators and engineers to obtaing valuable information about
performance impacts of the use of ``python-oneviewclient`` to access OneView,
and better understanding possible hotspots and bottle necks between Ironic
and OneView integration.

See an example of the audit output file::

 {
    "method": "get_node_power_state",
    "client_instance_id": 140396067361488,
    "initial_time": "2016-08-29T17:32:01.403420",
    "end_time": "2016-08-29T17:32:01.439126",
    "is_ironic_request": true,
    "is_oneview_request": false,
    "ret": "Off"
}
