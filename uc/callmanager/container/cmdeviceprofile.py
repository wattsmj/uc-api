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
Description: Call Manager Device Profile as a container object
'''

from uc.callmanager._abc import CMContainer

class CMDeviceProfile(CMContainer):
    'Call Manager Device Profile as a container object'

    _action = 'getDeviceProfile'
    _search = '<name>{profile}</name>'
    _returntags = ''

    def __init__(self, uri, admin_username, admin_password, **kwargs):
        'Initialise the object'
        super().__init__(
            uri=uri,
            admin_username=admin_username,
            admin_password=admin_password
        )
        if kwargs.get('prefix'):
            self.prefix = kwargs.get('prefix')
        else:
            self.prefix = "em_"

    def _format_search(self, item):
        'format self._action with the item'
        self._search = self._search.format(
            profile=f'{self.prefix}{item}'
        )
