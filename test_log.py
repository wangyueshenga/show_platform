import logging
import logging.config
import time
import os

logging.config.fileConfig('./config/logging.config')

logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message')
logger.warning('warn msg')
logger.error('error msg')
logger.critical('critical msg')