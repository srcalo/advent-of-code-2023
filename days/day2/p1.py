import re

colorMax = {
	'red': 12,
	'green': 13,
	'blue': 14
}

def isValid(s: str) -> int:
	game = [x.split(" ")[1:] for x in s.replace(",", "").split(";")]
	id = int(game[0][0][0:-1])
	game[0] = game[0][1:]

	for round in game:
		for i in range(0, len(round), 2):
			if int(round[i]) > colorMax[round[i+1]]:
				return 0
	return id

def sol(fname):
	sum = 0
	with open(fname) as f:
		for line in f:
			sum += isValid(line.strip("\n"))

	print(sum)
