# coding: utf-8

from coroutx import Coroutx
from config import config


app = Coroutx()  # simple:)


from .apis import index, grades
