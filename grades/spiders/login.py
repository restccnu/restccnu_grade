# coding: utf-8

import base64
import requests
from coroutx import request
from ..errors import ForbiddenError
from . import info_login_url
from . import info_login_test_url
from . import lib_login_url
from . import lib_login_test_url
from . import headers


# Authorization: Basic base64(sid:password)
def info_login():
    """
    这里是阻塞的重灾区...
    """
    LoginUrl = info_login_url
    TestUrl = info_login_test_url

    hashstr = request.headers.get('Authorization')
    base64_hashstr = hashstr[6:]
    id_password = base64.b64decode(base64_hashstr)
    sid, password = id_password.split(':')

    # for test
    s = requests.Session()
    s.post(LoginUrl, {
        'userName': sid, 'userPass': password
    }), headers

    r = s.get(TestUrl)
    if 'window.alert' in r.content:
        raise ForbiddenError
    else:
        return s, sid
