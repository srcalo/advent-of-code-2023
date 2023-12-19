import logging
import argparse

def init_logging():
	""" Initializes logging config """
	level = logging.DEBUG
	fmt = '[%(levelname)s] - %(message)s'
	logging.basicConfig(level=level, format=fmt)

	return logging.getLogger()
