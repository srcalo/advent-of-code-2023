import argparse
import logging
from utils.log import init_logging

if __name__ == "__main__":
	init_logging()

	ap = argparse.ArgumentParser()
	ap.add_argument("file")
	fname = vars(ap.parse_args())["file"]
	sum = 0
	schematic: list[str] = []
	with open(fname) as f:
		for line in f:
			schematic.append(line.strip("\n"))
	
	for i in range(len(schematic)):
		for j in range(len(schematic[0])):
			if not schematic[i][j].isnumeric() and not schematic[i][j].isdigit() and schematic[i][j] != ".":
				logging.debug(f'Found digit at ({i}, {j}): {schematic[i][j]}')
