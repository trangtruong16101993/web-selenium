import logging
logging.getLogger().setLevel(logging.DEBUG)

#region config logger
'''
customize logger
ref. https://stackoverflow.com/a/28330410/248616
'''
formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

#log to file
from datetime import datetime
import os
HEADLESS_HOME='%s/..' % os.path.abspath(os.path.dirname(__file__))
filename = '{HEADLESS_HOME}/_log_/vault/log{timestamp}.txt'.format(
    HEADLESS_HOME=HEADLESS_HOME,
    timestamp=datetime.now().strftime('%Y%m%d-%H%M%S'),
)
file_handler = logging.FileHandler(filename, mode='w')
file_handler.setFormatter(formatter)

#log to console
import sys
screen_handler = logging.StreamHandler(stream=sys.stdout)
screen_handler.setFormatter(formatter)

#set it
logging.getLogger().addHandler(file_handler)
logging.getLogger().addHandler(screen_handler)
#endregion config logger

#region log alias/shorthand name
def log(text):
    logging.info(text)
def debug(text):
    logging.debug(text)
l  = log
ld = debug

def log_level(level=logging.INFO):
    logging.getLogger().setLevel(level)
#endregion log alias/shorthand name
