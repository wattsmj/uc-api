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
Description: Call Manager Resource Abstract Base Class as a container
'''

from collections import Container
from abc import ABCMeta, abstractmethod
from uc.callmanager.AXL import response_as_bool
from .cmresource import CMResource


class CMContainer(CMResource, Container):
    '''
    A base Call Manager resource... phone, ext. mobility profile
    as a Container
    '''

    __metaclass__ = ABCMeta

    _action = ''
    _search = ''
    _returnedtags = ''

    @abstractmethod
    def _format_search(self, item):
        'format self._action with the item'

    def __contains__(self, item):
        '''
        Returns True if user has the resource
        '''
        # Format search
        self._format_search(item)
        # Do the POST and return the response
        status_code, _ = self._post(
            action=self._action,
            search=self._search,
            returnedtags=self._returnedtags
        )
        # Return the results as a bool
        try:
            return response_as_bool(status_code)
        except ValueError as ex:
            raise ex
