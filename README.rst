====================
python-oneviewclient
====================

Library to use OneView to provide nodes for Ironic

This library adds a layer of communication between Ironic and HP OneView and
abstracts the version of OneView in place.

* Free software: Apache license
* Documentation: http://docs.openstack.org/developer/python-oneviewclient
* Source: http://git.openstack.org/cgit/openstack/python-oneviewclient
* Bugs: http://bugs.launchpad.net/python-oneviewclient

Features
========

Auditing
^^^^^^^^

The auditing feature allows an user to audit OneView API calls made by using this client.

For run the audition, a configuration file is need and must be filled with the following up sections::

    # In audit section, must be placed case's name that going to be
    # used for the audition.

    [audit]
    case = requests

    # The cases section must contains a name that represent the case
    # and the names of the python-oneviewclient methods the will be
    # audited. The methods name needs to be separated by comma and
    # have no blank spaces between them.

    [cases]
    requests = _authenticate,verify_credentials,verify_oneview_version ...
    power_requests = get_node_power_state,power_on,power_off,set_node_power_state

After fill all the needed information, save the file with ``.conf`` extention.

Enable auditing
---------------

For enable auditing, three informations must be fill when instantiating a client:

* ``audit_enabled``
* ``audit_map_file``
* ``audit_output_file``

The first option, ``audit_enabled`` allows users to enable or disable the auditing process. The
``audit_map_file`` is the path to the conf file where the cases of auditing and the combinations
of methods to audit must be placed. The third and last one is ``audit_output_file``, it means
the path to the directory where the auditing result file will be placed.

To use the python-oneviewclient for auditing you must create an OneView Client instance like::

    oneview_client = client.ClientV2(
        manager_url='http://oneviewappliance.com',
        username='username',
        password='password',
        audit_enabled=True,
        audit_map_file='/some/path/oneview_audit_map.conf',
        audit_output_file='/some/path/oneview_audit_output.json'
    )

If the audition will be based on requests made by Ironic, those three parameters must be passed in
the ``ironic.conf`` file, in ``oneview`` section.

Running the auditing
--------------------

For run the auditing, since all configurations above were set, each call for methods that were
defined in the ``cases`` section in the configuration file and that was chosen as case for
auditing in the ``audit`` section, will be registered in the audit output file.
