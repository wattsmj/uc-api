'''
Call Manager Resource Abstract Base Class
as a container
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
