import logging
import logging.config
import time
import os
import sys
import yaml
def init_config():
	logging.config.fileConfig('config/logging.conf')


def fread(fname):
	with open(os.path.join(os.path.dirname(__file__),fname)) as fi:
		global content
		content = fi.read()
	return content


def log_fun():
	logger = logging.getLogger()
	logger.debug('debug message')
	logger.info('info message')
	logger.warning('warn message')
	logger.error('error message')
	logger.critical('critical message')



if __name__ == '__main__':
	# configfile = fread("config/logging.conf")
	# logger.info("begin")
	# contetn = fread("page\\index.htm")
	# logger.info("end")
	# print(content)
	# print(configfile)
	log_fun()