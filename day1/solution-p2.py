import regex as re
import argparse
words_to_numbers = {
	'one': '1',
	'two': '2',
	'three': '3',
	'four': '4',
	'five': '5',
	'six': '6',
	'seven': '7',
	'eight': '8',
	'nine': '9',
}

num = "\d|one|two|three|four|five|six|seven|eight|nine"
def findDigits(s: str) -> int:
	print(f'String: {s}')
	m = re.findall(num, s, overlapped=True)
	f = words_to_numbers.get(m[0], m[0])
	l = words_to_numbers.get(m[-1], m[-1])
	print(f'Num: {f + l}\n')
	return int(f + l)

if __name__ == "__main__":
	ap = argparse.ArgumentParser()
	ap.add_argument("file")
	fname = vars(ap.parse_args())["file"]
	sum = 0
	with open(fname) as f:
		for line in f:
			sum += findDigits(line.strip("\n"))
	print(sum)
