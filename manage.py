# coding: utf-8

import sys
from grades import app
from middlewares import ratelimit
from gevent.wsgi import WSGIServer
from gevent import monkey
monkey.patch_all()


if __name__ == '__main__':
    # 每15分钟300次请求限制
    host = 'localhost'; port = '8090'
    if len(sys.argv) > 1:
        host = sys.argv[1] 
        port = sys.argv[2]
    app.firing(host=host, port=int(port)) #, debug=True)
