'Call Manager Device Profile as a container object'

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
