'Call Manager Line as a model'

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
