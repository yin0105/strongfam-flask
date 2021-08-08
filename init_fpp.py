#! /home/brumey3/opt/python-3.8.5/bin/python
# -*- coding: UTF-8 -*-

from html import escape
import sys, os
from flup.server.fcgi import WSGIServer

def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/plain')])
    return ['Hello World!\n']

if __name__ == '__main__':
    from flup.server.fcgi import WSGIServer
    WSGIServer(app).run()