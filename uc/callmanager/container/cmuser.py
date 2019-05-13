'Call Manager User Resource as a container object'

from uc.callmanager._abc import CMContainer

class CMUser(CMContainer):
    'Call Manager User Resource as a container object'

    _action = 'getUser'
    _search = '<userid>{username}</userid>'
    _returnedtags = '<userid/>'

    def _format_search(self, item):
        'format self._action with the item'
        self._search = self._search.format(
            username=item
        )
