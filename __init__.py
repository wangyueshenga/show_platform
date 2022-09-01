# 127.0.0.1:1001/hello/
import os
import logging
import logging.config
import sys

global localhost, port, debug
localhost = '127.0.0.1'
port = 1001
debug = True

from flask import Flask

logger = logging.getLogger('flaskLogger')
logging.config.fileCongfig('config/logging.config')

def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_mapping(
		SECRET_KEY='dev',
		DATABASE=os.path.join(app.instance_path,'flask.sqilte'),
		)
	if test_config is None:
		app.config.from_pyfile('config.py', silent=True)
	else:
		app.config.from_mapping(test_config)
	try:
		os.makedirs(app.instance_path)
	except OSError as oe:


app = Flask("Hello world")


@app.route('/hello')
def hello_world():
	return 'Hello World.'


@app.route('/whatsup')
def whatsup():
	return 'what\'s up'


@app.route('/hello/<name>')
def hello_name(name):
	return 'hello %s!' % name


@app.route('/blog/<int:postID>')
def show_blog(postID):
	return 'BLOG NUM %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
	return 'Revision Number %f' % revNo


if __name__ == '__main__':
	app.run(localhost, port=port, debug=debug)