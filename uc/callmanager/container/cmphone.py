'Call Manager Phone as a container object'

from uc.callmanager._abc import CMContainer

class CMPhone(CMContainer):
    'Call Manager Phone as a container object'

    _action = 'getPhone'
    _search = '<name>{phone}</name>'
    _returntags = ''

    def _format_search(self, item):
        'format self._action with the item'
        self._search = self._search.format(
            phone=item
        )
