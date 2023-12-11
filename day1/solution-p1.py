import re

if __name__ == "__main__":
	sum = 0
	with open("day1/input.txt") as f:
		for line in f:
			d = re.findall('\d',line)
			sum += int(d[0] + d[-1])
	print(sum)
