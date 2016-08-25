# coding: utf-8

import json
from werkzeug.wrappers import BaseResponse as Response



class ForbiddenError(Exception):
    def __init__(self):
        self.status_code = 403

    def __repr__(self):
        return "{'msg': 'forbidden'}"


class NotfoundError(Exception):
    def __init__(self):
        self.status_code = 404

    def __repr__(self):
        return "{'msg': 'notfound'}"


class InternalServerError(Exception):
    def __init__(self):
        self.status_code = 500

    def __repr__(self):
        return "{'msg': 'server error'}"


def too_many_request():
    # response = Response(
    #     {'msg': 'to many requests...'},
    #     status=429)
    response = {'msg': 'too many requests...'}
    return response
