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

from abc import ABCMeta, abstractmethod
from uc.callmanager.AXL import response_as_bool
from .cmresource import CMResource


class CMModel(CMResource):
    '''
    A base Call Manager resource... phone, ext. mobility profile
    as a data model
    '''

    __metaclass__ = ABCMeta

    def __init__(self, uri, admin_username, admin_password, **kwargs):
        'Initialise the object'
        super().__init__(uri, admin_username, admin_password, **kwargs)
        self._data = None

    def __getattr__(self, item):
        'Returns values from the AXL API response as instance attributes'
        if self._data is not None:
            if self._data.find(item) is not None:
                return self._data.find(item).text

    @abstractmethod
    def _format_search(self):
        'Formats the search string'

    @abstractmethod
    def _format_returnedtags(self):
        'Formats the returnedtags string'

    @abstractmethod
    def _save_data(self, data):
        '''
        Save the AXL reponse to self._data
        as an XML element tree
        '''

    # @abstractmethod
    def get(self):
        '''
        Get the data for this line from call manager
        and save the data in self._data
        '''
        # format search criteria
        self._format_search()
        # format returnedtags
        self._format_returnedtags()
        # Do the POST
        status_code, response = self._post(
            action=self._action,
            search=self._search,
            returnedtags=self._returnedtags
        )
        # Save the response in self._data
        # Return the results as a bool
        try:
            if response_as_bool(status_code):
                self._save_data(response)
            else:
                raise ValueError(f'{self._error_line}')
        except ValueError as ex:
            raise ex
