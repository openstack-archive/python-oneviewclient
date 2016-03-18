import abc
import six
import oneview_api

class Resource(object):
    six.add_metaclass(abc.ABCMeta)

    def __init__(self, info):
        self._info = info
        self._add_details(info)

    def _add_details(self, info):
        for (k, v) in six.iteritems(info):
            try:
                setattr(self, k, v)
                self._info[k] = v
            except AttributeError:
                pass


class Network(Resource):
    def __repr__(self):
        return "<Network uri='%s'>" % self.uri

class ServerHardware(Resource):
    def __repr__(self):
        return "<ServerHardware uri='%s'>" % self.uri


class Manager(object):
    six.add_metaclass(abc.ABCMeta)
    api = None

    def __init__(self, oneview_api):
        self.oneview_api = oneview_api

    def _dict_to_object(self, dictionary):
        raise Exception('Not Implemented')

    def _object_to_dict(self, obj):
        raise Exception('Not Implemented')

    def create(self, obj):
        self.api.create(_object_to_dict(obj))

    def list(self):
        objects = []
        items = self.api.list()

        for item in items:
            objects.append(self._dict_to_object(item))

        return objects

    def get(self, uri):
        return self._dict_to_object(self.api.get(uri))


class NetworkManager(Manager):
    fields = ['uri', 'name']

    def _dict_to_object(self, dict):
        filtered_server_profile_dict = {}
        for field in self.fields:
            filtered_server_profile_dict[field] = dict[field]
        return Network(filtered_server_profile_dict)


class ServerHardwareManager(Manager):
    fields = ['uri', 'serverHardwareTypeUri', 'uuid', 'memoryMb',
              'description', 'serverGroupUri', 'name', 'serverProfileUri']

    def __init__(self, oneview_api):
        super(ServerHardwareManager, self).__init__(oneview_api)
        self.api = self.oneview_api.server_hardware

    def create(self, obj):
        raise Exception('Not Supported')

    def _object_to_dict(self, obj):
        pass

    def _dict_to_object(self, dict):
        filtered_server_profile_dict = {}
        for field in self.fields:
            filtered_server_profile_dict[field] = dict[field]

        """
        filtered_server_profile_dict['cpus'] = dict['processorCoreCount'] * \
            dict['processorCount']
        filtered_server_profile_dict['cpu_arch'] = 'x86_64'
        filtered_server_profile_dict['local_gb'] = 120

        filtered_server_profile_dict['serverHardwareTypeName'] = \
            self.oneviewclient.server_hardware_type.get(
                filtered_server_profile_dict['serverHardwareTypeUri'], 'name')
        filtered_server_profile_dict['serverGroupName'] = \
            self.oneviewclient.enclosure_group.get(
                filtered_server_profile_dict['serverGroupUri'], 'name')

        print filtered_server_profile_dict
        """
        return ServerHardware(filtered_server_profile_dict)


class OneViewClient(object):
    def __init__(
        self, manager_url, username, password,
        allow_insecure_connections=False, tls_cacert_file=''
    ):
        self.oneview_api = oneview_api.OneViewAPI(
            manager_url=manager_url, username=username, password=password,
            allow_insecure_connections=allow_insecure_connections,
            tls_cacert_file=tls_cacert_file
        )
        self.server_hardware = ServerHardwareManager(self.oneview_api)
        self.network = NetworkManager(self.oneview_api)


url = "https://150.165.85.176"
c = OneViewClient(url, 'administrator', '1r0n1c@LSD')
l = c.server_hardware.list()
print c.server_hardware.get(l[0].uri)
