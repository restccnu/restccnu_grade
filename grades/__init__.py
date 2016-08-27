# coding: utf-8

import redis
from coroutx import Coroutx
from config import config


app = Coroutx()  # simple:)


from .apis import index, grades
