'Call Manager Phone as a container object'

from uc.callmanager._abc import CMContainer

class CMLine(CMContainer):
    'Call Manager Phone as a container object'

    _action = 'getLine'
    _search = '''<pattern>{pattern}</pattern>
    <routePartitionName>{partition}</routePartitionName>'''
    _returnedtags = ''

    def __init__(self, uri, admin_username, admin_password, **kwargs):
        'Initialise the object'
        super().__init__(uri, admin_username, admin_password, **kwargs)
        self._partition = kwargs.get('partition', None)

    def _format_search(self, item):
        'format self._action with the items'
        self._search = self._search.format(
            pattern=item,
            partition=self._partition
        )
