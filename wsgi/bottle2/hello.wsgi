import os
import bottle
os.chdir(os.path.dirname(__file__))

from bottle import route, run

@route('/hello')
def hello():
    return "Hello World2!"

application = bottle.default_app()
