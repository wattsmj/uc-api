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
Description: Call Manager Jabber as a container object
'''

from .cmphone import CMPhone

class CMJabber(CMPhone):
    'Call Manager Jabber as a container object'

    _search = '<name>csf{phone}</name>'
