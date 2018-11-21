from sys import argv
import bottle
from bottle import *

@route('/')
def index():
    return template('index')

@route('/innskra')
def innskra():
    return template('innskra')

@route('/nyskra')
def nyskra():
    return template('nyskra')
    
##########################################
@error(404)
def villa(error):
    return "<h2>Error 404: Not Found</h2>"

@route("/static/<skra>")
def static_skra(skra):
    return static_file(skra, root="./static")

run(host='localhost', port=8080, reloader=True)

#bottle.run(host="0.0.0.0", port=argv[1])
