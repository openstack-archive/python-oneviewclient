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

``python-oneviewclient`` is capable of logging method calls to OneView for
auditing. Currently, data about request timing and method names, parameters and
return values, can be recorded to be used in the auditing process to discover
and better understand hotspots, bottlenecks and to measure how the user code
and OneView integration performs.

Enabling audit logging
""""""""""""""""""""""

To enable audit logging, the user code has to set three parameters in the
constructor of the client object. namely: ``audit_enabled``, ``audit_map_file``
and ``audit_output_file``. ``audit_map_file`` and ``audit_output_file`` must be
filled with the absolute path to the audit map file and the audit output file.

The audit map file
""""""""""""""""""

The audit map file is composed of two sections, ``audit`` and ``cases``. In the
``audit`` section there should be a ``case`` option where one, and just one, of
the audit logging ``cases`` needs to be specified. The ``cases`` section needs
to be filled with a name for a case followed by the methods that the user wants
to audit logging. The methods that are allowed for the audit logging are those
decorated by ``@auditing.audit`` in ``python-oneviewclient``.

See an example of an audit map file::

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

The result of the audit logging process is a JSON formatted file that can be
used by auditors, operators and engineers to obtain valuable information about
performance impacts of using ``python-oneviewclient`` to access OneView,
and better understand possible hotspots and bottlenecks in the integration of
the user code and OneView.

See an example of an audit output file::

    {
        "method": "get_node_power_state",
        "client_instance_id": 140396067361488,
        "initial_time": "2016-08-29T17:32:01.403420",
        "end_time": "2016-08-29T17:32:01.439126",
        "is_ironic_request": true,
        "is_oneview_request": false,
        "ret": "Off"
    }
