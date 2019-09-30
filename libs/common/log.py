import logging
import sys
import libs.common.config as cfg

logger = None
logger_name = cfg.LOGGER_NAME
level = cfg.LOG_LEVEL
log_file = cfg.LOG_FILE_NAME

def init():
	global logger
	logger = logging.getLogger(logger_name)
	logger.setLevel(level)
	
	formatter = logging.Formatter(fmt='%(asctime)s : %(levelname)s : %(message)s', datefmt= '%Y-%m-%d %H:%M:%S')

	file_handler = logging.FileHandler(log_file)
	file_handler.setFormatter(formatter)

	strem_handler = logging.StreamHandler()
	strem_handler.setFormatter(formatter)

	logger.addHandler(strem_handler)
	logger.addHandler(file_handler)

def debug(msg):
	logger.debug(msg)

def info(msg):
	logger.info(msg)

def warn(msg):
	logger.warning(msg)

def error(msg):
	logger.exception(msg)

def critical(msg):
	logger.critical(msg)
	sys.exit("Its a critical situation, can't proceed further")