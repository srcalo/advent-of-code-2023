import re

if __name__ == "__main__":
	sum = 0
	with open("day1/input.txt") as f:
		for line in f:
			f = re.findall('\d',line)
			sum += int(f[0] + f[-1])
	print(sum)
