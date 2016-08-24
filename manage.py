# coding: utf-8

from grades import app
from gevent import monkey
monkey.patch_all()


if __name__ == '__main__':
    app.firing(debug=True)
