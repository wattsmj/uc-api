'AXL HTTP Status Function'

def response_as_bool(status_code):
    '''
    Returns the HTTP status code as a bool
    as per the AXL API: True for 200, False for 500
    or raises a ValueError for any other value
    '''
    if status_code == 200:
        return True
    elif status_code == 500:
        return False
    else:
        raise ValueError('username or access rights are invalid')
