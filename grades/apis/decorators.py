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
from .ratelimit import RateLimit


def require_info_login(f):
    @functools.wraps(f)
    def decorator(*args, **kwargs):
        try:
            s, sid = info_login()  # 阻塞IO
        except ForbiddenError as e:
            return json.dumps({}), e.status_code
        rv = f(s, sid, *args, **kwargs)
        return rv
    return decorator


def ratelimit(limit, per):
    def decorator(f):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            key = '{0}/{1}'.format(f.__name__, request.remote_addr)
            # key -> key prefix
            limiter = RateLimit(key, limit, per)
            # X-RateLimit-Headers 处理: 需要改造成中间件
            if limiter.over_limit:
                raise Exception
            return f(*args, **kwargs)
        return wrapper
    return decorator
