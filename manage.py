# coding: utf-8

from grades import app
from middlewares import ratelimit
from gevent.wsgi import WSGIServer
from gevent import monkey
monkey.patch_all()


if __name__ == '__main__':
	# 每15分钟300次请求
	grade = ratelimit.RateLimit(app, limit=300, per=60*15)
	WSGIServer(('localhost', 8090), grade).serve_forever()