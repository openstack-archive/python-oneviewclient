from __future__ import print_function
 # Copyright 2014,2015 Hewlett Packard Enterprise Development, LP.
 #
 # Licensed under the Apache License, Version 2.0 (the "License"); you may
 # not use this file except in compliance with the License. You may obtain
 # a copy of the License at
 #
 #      http://www.apache.org/licenses/LICENSE-2.0
 #
 # Unless required by applicable law or agreed to in writing, software
 # distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 # WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 # License for the specific language governing permissions and limitations
 # under the License.



import sys
import ssl
if (sys.version_info >= (3, 0)):
   # Python 3 imports
   from urllib.parse import urlparse
   from http.client import HTTPSConnection, HTTPConnection
   from io import StringIO
else:
   # Python 2 imports
   from urlparse import urlparse
   from httplib import HTTPSConnection, HTTPConnection
   from StringIO import StringIO

import base64
import json
import hashlib
import gzip
import re

# REST operation generic handler
def rest_op(operation, host, suburi, request_headers, request_body, x_auth_token, enforce_SSL=True):

    url = urlparse('https://' + host + suburi)
    # url = urlparse('http://' + host + suburi)

    if request_headers is None:
        request_headers = dict()

    # if X-Auth-Token specified, supply it instead of basic auth
    if x_auth_token is not None:
        request_headers['X-Auth-Token'] = x_auth_token
    # else use iLO_loginname/iLO_password and Basic Auth
    elif iLO_loginname is not None and iLO_password is not None:
        request_headers['Authorization'] = "BASIC " + base64.b64encode(iLO_loginname + ":" + iLO_password)

    redir_count = 4
    while redir_count:
        conn = None
        if url.scheme == 'https':
            # New in Python 2.7.9, SSL enforcement is defaulted on, but can be opted-out of.
            # The below case is the Opt-Out condition and should be used with GREAT caution.
            if(sys.version_info.major == 2 and
                sys.version_info.minor == 7 and
                sys.version_info.micro >= 9 and
                enforce_SSL == False):
                cont = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
                cont.verify_mode = ssl.CERT_NONE
                conn = HTTPSConnection(host=url.netloc, strict=True, context=cont)
            else:
                conn = HTTPSConnection(host=url.netloc, strict=True)
        elif url.scheme == 'http':
            conn = HTTPConnection(host=url.netloc, strict=True)
        else:
            assert(False)
        conn.request(operation, url.path, headers=request_headers, body=json.dumps(request_body))
        resp = conn.getresponse()
        body = resp.read()

        # NOTE:  Do not assume every HTTP operation will return a JSON body.  For example, ExtendedError structures
        # are only required for HTTP 400 errors and are optional elsewhere as they are mostly redundant for many of the
        # other HTTP status code.  In particular, 200 OK responses should not have to return any body.

        # NOTE:  this makes sure the headers names are all lower cases because HTTP says they are case insensitive
        headers = dict((x.lower(), y) for x, y in resp.getheaders())
        print(request_headers)
        print("\n\n")

        # Follow HTTP redirect
        if resp.status >= 300 and resp.status < 400 and 'location' in  headers:
            url = urlparse(headers['location'])
            redir_count -= 1
        else:
            break

    response = dict()
    try:
        response = json.loads(body.decode('utf-8'))
    except ValueError:  # if it doesn't decode as json
        # NOTE:  resources may return gzipped content
        # try to decode as gzip (we should check the headers for Content-Encoding=gzip)
        try:
            gzipper = gzip.GzipFile(fileobj=StringIO(body))
            uncompressed_string = gzipper.read().decode('UTF-8')
            response = json.loads(uncompressed_string)
        except:
            pass

        # return empty
        pass

    return resp.status, headers, response

# REST GET
def rest_get(host, suburi, request_headers, x_auth_token):
    return rest_op('GET', host, suburi, request_headers, None, x_auth_token)
    # NOTE:  be prepared for various HTTP responses including 500, 404, etc.

# REST PATCH
def rest_patch(server, suburi, request_headers, request_body, iLO_loginname, iLO_password):
    if not isinstance(request_headers, dict):  request_headers = dict()
    request_headers['Content-Type'] = 'application/json'
    return rest_op('PATCH', server, suburi, request_headers, request_body, iLO_loginname, iLO_password)
    # NOTE:  be prepared for various HTTP responses including 500, 404, 202 etc.

# REST PUT
def rest_put(host, suburi, request_headers, request_body, iLO_loginname, iLO_password):
    if not isinstance(request_headers, dict):  request_headers = dict()
    request_headers['Content-Type'] = 'application/json'
    return rest_op('PUT', host, suburi, request_headers, request_body, iLO_loginname, iLO_password)
    # NOTE:  be prepared for various HTTP responses including 500, 404, 202 etc.

# REST POST
def rest_post(host, suburi, request_headers, request_body, iLO_loginname, iLO_password):
    if not isinstance(request_headers, dict):  request_headers = dict()
    request_headers['Content-Type'] = 'application/json'
    return rest_op('POST', host, suburi, request_headers, request_body, iLO_loginname, iLO_password)
    # NOTE:  don't assume any newly created resource is included in the response.  Only the Location header matters.
    # the response body may be the new resource, it may be an ExtendedError, or it may be empty.

# REST DELETE
def rest_delete(host, suburi, request_headers, iLO_loginname, iLO_password):
    return rest_op('DELETE', host, suburi, request_headers, None, iLO_loginname, iLO_password)
    # NOTE:  be prepared for various HTTP responses including 500, 404, etc.
    # NOTE:  response may be an ExtendedError or may be empty

# this is a generator that returns collection members
def collection(host, collection_uri, request_headers, x_auth_token):

    # get the collection
    status, headers, thecollection = rest_get(host, collection_uri, request_headers, x_auth_token)

    while status < 300:

        # verify expected type

        # NOTE:  Because of the Redfish standards effort, we have versioned many things at 0 in anticipation of
        # them being ratified for version 1 at some point.  So this code makes the (unguarranteed) assumption
        # throughout that version 0 and 1 are both legitimate at this point.  Don't write code requiring version 0 as
        # we will bump to version 1 at some point.

        # hint:  don't limit to version 0 here as we will rev to 1.0 at some point hopefully with minimal changes
        assert(get_type(thecollection) == 'Collection.0' or get_type(thecollection) == 'Collection.1')

        # if this collection has inline items, return those

        # NOTE:  Collections are very flexible in how the represent members.  They can be inline in the collection
        # as members of the 'Items' array, or they may be href links in the links/Members array.  The could actually
        # be both.  Typically, iLO implements the inline (Items) for only when the collection is read only.  We have
        # to render it with the href links when an array contains PATCHable items because its complex to PATCH
        # inline collection members.
        # A client may wish to pass in a boolean flag favoring the href links vs. the Items in case a collection
        # contains both.

        if 'Items' in thecollection:

            # iterate items
            for item in thecollection['Items']:
                # if the item has a self uri pointer, supply that for convenience
                memberuri = None
                if 'links' in item and 'self' in item['links']:
                    memberuri = item['links']['self']['href']

                # Read up on Python generator functions to understand what this does.
                yield 200, None, item, memberuri

        # else walk the member links
        elif 'links' in thecollection and 'Member' in thecollection['links']:

            # iterate members
            for memberuri in thecollection['links']['Member']:
                # for each member return the resource indicated by the member link
                status, headers, member = rest_get(host, memberuri['href'], request_headers, x_auth_token)

                # Read up on Python generator functions to understand what this does.
                yield status, headers, member, memberuri['href']

        # page forward if there are more pages in the collection
        if 'links' in thecollection and 'NextPage' in thecollection['links']:
            next_link_uri = collection_uri + '?page=' + str(thecollection['links']['NextPage']['page'])
            status, headers, thecollection = rest_get(host, next_link_uri, request_headers, x_auth_token)

        # else we are finished iterating the collection
        else:
            break

# return the type of an object (down to the major version, skipping minor, and errata)
def get_type(obj):
    typever = obj['Type']
    typesplit = typever.split('.')
    return typesplit[0] + '.' + typesplit[1]

# checks HTTP response headers for specified operation (e.g. 'GET' or 'PATCH')
def operation_allowed(headers_dict, operation):
    if 'allow' in headers_dict:
        if headers_dict['allow'].find(operation) != -1:
            return True
    return False

# Message registry support
message_registries = {}

# Build a list of decoded messages from the extended_error using the message registries
# An ExtendedError JSON object is a response from the with its own schema.  This function knows
# how to parse the ExtendedError object and, using any loaded message registries, render an array of
# plain language strings that represent the response.
def render_extended_error_message_list(extended_error):
    messages = []
    if isinstance(extended_error, dict):
        if 'Type' in extended_error and extended_error['Type'].startswith('ExtendedError.'):
            for msg in extended_error['Messages']:
                MessageID = msg['MessageID']
                x = MessageID.split('.')
                registry = x[0]
                msgkey = x[len(x) - 1]

                # if the correct message registry is loaded, do string resolution
                if registry in message_registries:
                    if registry in message_registries and msgkey in message_registries[registry]['Messages']:
                        msg_dict = message_registries[registry]['Messages'][msgkey]
                        msg_str = MessageID + ':  ' + msg_dict['Message']

                        for argn in range(0, msg_dict['NumberOfArgs']):
                            subst = '%' + str(argn + 1)
                            msg_str = msg_str.replace(subst, str(msg['MessageArgs'][argn]))

                        if 'Resolution' in msg_dict and msg_dict['Resolution'] != 'None':
                            msg_str += '  ' + msg_dict['Resolution']

                        messages.append(msg_str)
                else:  # no message registry, simply return the msg object in string form
                    messages.append('No Message Registry Info:  ' + str(msg))

    return messages

# Print a list of decoded messages from the extended_error using the message registries
def print_extended_error(extended_error):
    messages = render_extended_error_message_list(extended_error)
    msgcnt = 0
    for msg in messages:
        print('\t' + msg)
        msgcnt += 1
    if msgcnt == 0:  # add a spacer
        print()

