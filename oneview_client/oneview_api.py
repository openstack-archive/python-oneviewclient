import requests
import json


requests.packages.urllib3.disable_warnings()

ONEVIEW_REST_API_VERSION = '200'

GET_REQUEST_TYPE = 'GET'
PUT_REQUEST_TYPE = 'PUT'
POST_REQUEST_TYPE = 'POST'
DELETE_REQUEST_TYPE = 'DELETE'

AUTHENTICATION_URI = '/rest/login-sessions'
SERVER_HARDWARE_PREFIX_URI = '/rest/server-hardware/'
SERVER_PROFILE_TEMPLATE_PREFIX_URI = '/rest/server-profile-templates/'


class OneViewRequestAPI(object):
    def __init__(
        self, manager_url, username, password,
        allow_insecure_connections=True, tls_cacert_file='',
        max_polling_attempts=20
    ):
        self.manager_url = manager_url
        self.username = username
        self.password = password
        self.allow_insecure_connections = allow_insecure_connections
        self.tls_cacert_file = tls_cacert_file
        self.max_polling_attempts = max_polling_attempts

        self.session_id = self._get_new_token()

    def _get_ca_certificate(self):
        if not self.allow_insecure_connections:
            return self.tls_cacert_file
        return False

    def _get_new_token(self):
        uri = "%s%s" %(self.manager_url, AUTHENTICATION_URI)
        headers = {'content-type': 'application/json'}
        body = {
            'password': self.password,
            'userName': self.username
        }
        response = requests.request(
            POST_REQUEST_TYPE,  uri, headers=headers, data=json.dumps(body),
            verify=self._get_ca_certificate()
        )
        return response.json()['sessionID']

    def prepare_and_execute_request(self, uri, body={}, request_type='GET'):
        headers = {
            'content-type': 'application/json',
            'X-Api-Version': ONEVIEW_REST_API_VERSION,
            'Auth': self.session_id
        }
        url = '%s%s' % (self.manager_url, uri)
        response = requests.request(
            request_type, url, headers=headers, data=json.dumps(body),
            verify=self._get_ca_certificate()
        )
        return response.json()


class OneViewResourceAPI(OneViewRequestAPI):
    resource_prefix_uri = None

    def create(self, body):
        return self.prepare_and_execute_request(
            self.resource_prefix_uri, body=body, request_type=POST_REQUEST_TYPE
        )

    def list(self):
        items_dict = self.prepare_and_execute_request(self.resource_prefix_uri)
        return items_dict['members']

    def get(self, uri):
        return self.prepare_and_execute_request(uri)


class OneViewServerHardware(OneViewResourceAPI):
    resource_prefix_uri = SERVER_HARDWARE_PREFIX_URI


class OneViewNetwork(OneViewResourceAPI):
    resource_prefix_uri = NETWORK_PREFIX_URI


class OneViewAPI(object):
    def __init__(
        self, manager_url, username, password,
        allow_insecure_connections=True, tls_cacert_file='',
        max_polling_attempts=20
    ):
        self.server_hardware = OneViewServerHardware(
            manager_url=manager_url, username=username, password=password,
            allow_insecure_connections=allow_insecure_connections,
            tls_cacert_file=tls_cacert_file
        )

#url = "https://150.165.85.176"
#c = OneViewRequestAPI(url, 'administrator', '1r0n1c@LSD')
#sh = OneViewServerHardware(url, 'administrator', '1r0n1c@LSD')
#print sh.get()
#body = {'userName': 'administrator', 'password': '1r0n1c@LSD'}
#headers = {'content-type': 'application/json'}
#print requests.post(
#    "https://150.165.85.176/rest/login-sessions", headers=headers, data=json.dumps(body), verify=False).json()
