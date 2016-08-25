# coding: utf-8

import redis
from coroutx import Coroutx
from config import config


app = Coroutx()  # simple:)
rate = redis.StrictRedis(host='localhost', port=6386, db=0) # for rate limit


from .apis import index, grades
