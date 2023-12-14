import logging

def init_logging():
	level = logging.DEBUG
	fmt = '[%(levelname)s] - %(message)s'
	logging.basicConfig(level=level, format=fmt)
