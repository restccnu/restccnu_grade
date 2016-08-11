# coding: utf-8

import os
from datetime import timedelta


class Config(object):

    XNM = 2015
    XQM = 12


config = {
    'develop': Config,
    'test': Config,

    'default': Config
}
