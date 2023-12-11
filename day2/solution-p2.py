import re



def powerMin(s: str) -> int:
	game = [x.split(" ")[1:] for x in s.replace(",", "").split(";")]
	game[0] = game[0][1:]
	colorMax = {
		'red': 0,
		'green': 0,
		'blue': 0
	}
	for round in game:
		for i in range(0, len(round), 2):
			colorMax[round[i+1]] = max(colorMax[round[i+1]], int(round[i]))
	return colorMax['red'] * colorMax['green'] * colorMax['blue']

if __name__ == "__main__":
	sum = 0
	with open("day2/input.txt") as f:
		for line in f:
			sum += powerMin(line.strip("\n"))

	print(sum)
