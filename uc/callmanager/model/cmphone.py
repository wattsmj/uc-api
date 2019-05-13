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
Description: Call Manager Line as a model
'''

import xml.etree.ElementTree as ET
from uc.callmanager._abc import CMModel


class CMPhone(CMModel):
    'Call Manager Line as a model'

    _error_line = 'Phone not found'
    _action = 'getPhone'
    _search = '''
    <name>{pattern}</name>'''
    _returnedtags = ''

    def __init__(self, uri, admin_username, admin_password, **kwargs):
        'Initialise the object'
        super().__init__(uri, admin_username, admin_password, **kwargs)
        self._pattern = kwargs.get('pattern', None)
        self._tags = kwargs.get('tags', [])
        self._xml = None

    def _format_search(self):
        'Formats the search string'
        self._search = self._search.format(
            pattern=self._pattern,
        )

    def _format_returnedtags(self):
        'Formats the returnedtags string'
        template = '<{tag}/>'
        self._returnedtags += '\n'.join(
            [template.format(tag=item) for item in self._tags]
        )

    def _save_data(self, data):
        '''
        Save the AXL reponse to self._data
        as an XML element tree
        '''
        root = ET.fromstring(data)
        self._xml = data
        # Body > GetLineResponse > return > phone
        line_root = root[0][0][0][0]
        self._data = line_root
