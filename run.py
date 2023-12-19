import sys
import os
import argparse
import importlib
import importlib.util

if __name__ == "__main__":
	ap = argparse.ArgumentParser(description="Run Advent of Code problems")
	ap.add_argument("day", metavar="Day", type=int, choices=range(1,26), help="The advent calendar day; takes 1 through 25")
	ap.add_argument("part", metavar="Part", type=int, choices=[1,2], help="The problem for the given day to run; takes 1 or 2")
	ap.add_argument("-t", "--test", default="input", help="What test to run the problem on; takes any existing test; if not provided, will default to problem input")
	args = vars(ap.parse_args())

	mod = importlib.import_module(f'..p{args["part"]}',f'days.day{args["day"]}.p1')

	mod.sol(f'days\day{args["day"]}\{args["test"]}.txt')
