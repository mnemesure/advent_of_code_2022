import pandas as pd
import numpy as np

with open("day6.txt") as f:
	data = f.read()

def window_checker(seq):
	if len(set(seq)) == len(seq):
		return True
	else:
		return False

if __name__ == "__main__":

	WINDOW_RANGE = 4

	for window in range(len(data)):
		sequence = data[window:window+WINDOW_RANGE]
		test = window_checker(sequence)

		if test:
			print(f"Part1: {window+WINDOW_RANGE}")
			break

	WINDOW_RANGE=14

	for window in range(len(data)):
		sequence = data[window:window+WINDOW_RANGE]
		test = window_checker(sequence)

		if test:
			print(f"Part2: {window+WINDOW_RANGE}")
			break
