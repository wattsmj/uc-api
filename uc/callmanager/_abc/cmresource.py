'''
Searches Call Manager for resources (user, jabber phone, ext. mobility profile) and reports on what is present.
Copyright (C) 2019  Matthew Watts

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.

Author: wattsmj
Contact: Please raise an issue on www.github.com/wattsmj/uc-api
Description: Call Manager Resource Abstract Base Class
'''

from abc import ABCMeta
from requests.auth import HTTPBasicAuth
import requests


class CMResource(object):
    '''
    A base Call Manager resource... phone, ext. mobility profile
    '''

    __metaclass__ = ABCMeta

    _content_type = 'text/xml'
    _SOAP_action = "CUCM:DB ver=11.0"
    _SOAP_text = '''
    <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns="http://www.cisco.com/AXL/API/11.0">
        <soapenv:Header/>
        <soapenv:Body>
            <ns:{action}>
            {search}
            <returnedTags>
                {returntags}
            </returnedTags>
            </ns:{action}>
        </soapenv:Body>
    </soapenv:Envelope>
    '''

    def __init__(self, uri, admin_username, admin_password, **kwargs):
        'Initialise the object'
        self._uri = uri
        self._admin_username = admin_username
        self._admin_password = admin_password
        self._data = None
        self._last_post = None

    def _headers(self):
        '''
        Returns the HTTP headers as a dictionary
        '''
        return {
            "SOAPAction": self._SOAP_action,
            'Content-Type': self._content_type
        }

    def _auth(self):
        '''
        Returns a request authentication object
        '''
        return HTTPBasicAuth(
            self._admin_username,
            self._admin_password
        )

    def _format(self, action, search, returnedtags, **kwargs):
        '''
        Returns the SOAP query text formatted with the given variables
        '''
        formatdict = {
            'action': action,
            'search': search,
            'returntags': returnedtags
        }
        formatdict.update(**kwargs)
        return self._SOAP_text.format(**formatdict)

    def _post(self, action, search, returnedtags, **kwargs):
        '''
        Returns the SOAP response to the given
        soap_action from the Cisco AXL interface
        '''
        # HTTP headers
        headers = self._headers()
        # HTTP Basic autentication
        auth = self._auth()
        # Do necessary formats
        soap_text = self._format(
            action=action,
            search=search,
            returnedtags=returnedtags,
            **kwargs
        )
        # Do a HTTP POST, return the HTTP status code
        # and body text
        self._last_post = soap_text
        resp = requests.post(
            self._uri,
            auth=auth,
            headers=headers,
            data=soap_text,
            verify=False
        )
        return (resp.status_code, resp.text)
