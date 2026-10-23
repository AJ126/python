
# Write a Python program to create a log file
# and write WARNING and higher-level messages.

import logging

logging.basicConfig(filename='log.txt', level=logging.WARNING, format='%(levelname)s: %(message)s')

print('Logging module demo')

logging.warning('Warning message')
logging.error('Error message')
logging.info('Info message')
logging.critical('Critical message')
logging.debug('Debug message')
