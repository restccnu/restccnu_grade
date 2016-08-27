# coding: utf-8

import os
import json
import base64
import functools
import json
import gevent
from coroutx import request, current_app
from ..spiders.login import info_login
from ..errors import ForbiddenError, too_many_request


def require_info_login(f):
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        try:
            _s, s, sid = info_login()  # requests阻塞IO
        except ForbiddenError as e:
            return json.dumps({}), e.status_code
        rv = f(_s, s, sid, *args, **kwargs)
        return rv
    return decorator