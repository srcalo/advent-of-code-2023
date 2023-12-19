import re

def sol(fname):
	sum = 0
	with open(fname) as f:
		for line in f:
			d = re.findall('\d',line)
			sum += int(d[0] + d[-1])
	print(sum)
