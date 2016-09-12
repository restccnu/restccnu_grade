# coding: utf-8

import base64
from requests import Session
from requests_futures.sessions import FuturesSession
from coroutx import request
from ..errors import ForbiddenError
from . import info_login_url
from . import info_login_test_url
from . import lib_login_url
from . import lib_login_test_url
from . import headers, proxy


# Authorization: Basic base64(sid:password)
def info_login():
    """
    信息门户登录
    """
    LoginUrl = info_login_url
    TestUrl = info_login_test_url

    hashstr = request.headers.get('Authorization')
    base64_hashstr = hashstr[6:]
    id_password = base64.b64decode(base64_hashstr)
    sid, password = id_password.split(':')

    _s = Session()
    _s.post(LoginUrl, {
        'userName': sid, 'userPass': password
    }, headers=headers, proxies=proxy)

    r = _s.get(TestUrl)
    if 'window.alert' in r.content:
        raise ForbiddenError
    else:
        s = FuturesSession(session=_s)
        return _s, s, sid
