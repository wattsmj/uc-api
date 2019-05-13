'Call Manager Jabber as a container object'

from .cmphone import CMPhone

class CMJabber(CMPhone):
    'Call Manager Jabber as a container object'

    _search = '<name>csf{phone}</name>'
