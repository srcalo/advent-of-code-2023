import logging
import argparse

def init_logging():
	""" Initializes logging config """
	level = logging.DEBUG
	fmt = '[%(levelname)s] - %(message)s'
	logging.basicConfig(level=level, format=fmt)

def parse_args() -> tuple[str, dict[str, str]]:
	""" Parses args and returns file passed in separate from other args """
	ap = argparse.ArgumentParser()
	ap.add_argument("file")
	args = vars(ap.parse_args())
	return (args["file"], args)
