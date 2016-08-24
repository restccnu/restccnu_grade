# coding: utf-8

import os
import json
import base64
import functools
import json
import gevent
from coroutx import request
from ..spiders.login import info_login
from ..errors import ForbiddenError


def require_info_login(f):
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        try:
            s, sid = info_login()
        except ForbiddenError as e:
            return json.dumps({}), e.status_code
        else:
            rv = f(s, sid, *args, **kwargs)
            return rv
    return decorator