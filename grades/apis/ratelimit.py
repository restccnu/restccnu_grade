# coding: utf-8

import time
from .. import rate


class RateLimit(object):
    expiration_window = 10

    def __init__(self, key_prefix, limit, per):
        """
        key_prefix: unique id for ip and function
        """
        self.reset = (int(time.time()) // per) * per + per
        self.key = key_prefix + str(self.reset)
        self.limit = limit
        self.per = per
        p = rate.pipeline()
        p.incr(self.key)  # incr key(unique for each client)
        p.expireat(self.key, self.reset + self.expiration_window) # set expireat
        self.current = p.execute()[0]

    remaining = property(lambda x: x.limit - x.current)
    over_limit = property(lambda x: x.current >= x.limit)
