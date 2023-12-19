import logging
from util import init_logging

def sol(fname):
	init_logging()

	sum = 0
	schematic: list[str] = []
	with open(fname) as f:
		for line in f:
			schematic.append(line.strip("\n"))
	
	for i in range(len(schematic)):
		for j in range(len(schematic[0])):
			if not schematic[i][j].isnumeric() and not schematic[i][j].isdigit() and schematic[i][j] != ".":
				logging.debug(f'Found digit at ({i}, {j}): {schematic[i][j]}')
