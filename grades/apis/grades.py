# coding: utf-8

from .. import app
from .decorators import require_info_login
from ..spiders.grade import get_grade, get_grade_detail
from coroutx import request, current_app, route


@route(app, '/api/info/login/')
@require_info_login
@app.tojson
def api_info_login(s, sid):
    return {}


@route(app, '/api/grade/search/')
@require_info_login  # <-*
@app.tojson
def api_get_grade(_s, s, sid):
    xnm = request.args.get('xnm')
    xqm = request.args.get('xqm')
    # return get_grade(s, sid, xnm, xqm)
    return get_grade(_s, s, sid, xnm, xqm)


@route(app, '/api/grade/detail/search/')
@require_info_login
@app.tojson
def api_get_detail_grade(_s, s, sid):
    xnm = request.args.get('xnm')
    xqm = request.args.get('xqm')
    course = request.args.get('course')
    jxb_id = request.args.get('jxb_id')
    return get_grade_detail(_s, s, sid, xnm, xqm, course, jxb_id)
