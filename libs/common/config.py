import os

#GENERAL
VERBOSITY = False

#LOG related configs
LOGGER_NAME = 'Auto'
LOG_FILE_NAME = 'default.log'
LOG_LEVEL = 'DEBUG'

#DIRS
HOME_DIR = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-3])
BIN_DIR = HOME_DIR + os.sep + 'bin'
TOOLS_DIR = HOME_DIR + os.sep + 'tools'
SCRIPTS_DIR = HOME_DIR + os.sep + 'scripts'
RESULT_DIR = HOME_DIR + os.sep + 'results'

PROJ_DIR = HOME_DIR + os.sep + 'scripts' + os.sep + 'projects'
SUITE_DIR = HOME_DIR + os.sep + 'scripts' + os.sep + 'suites'
