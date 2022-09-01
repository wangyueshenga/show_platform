import logging
import logging.config
import time
import os
import sys
import yaml

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p ')

logging.info('1')
logger = logging.getLogger()

def fread(fname):
	with open(os.path.join(os.path.dirname(__file__),fname)) as fi:
		global content

		content = fi.read()
	return content

if __name__ == '__main__':
	logger.info("begin")
	contetn = fread("page\\index.htm")
	logger.info("end")
	print(content)