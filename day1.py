import numpy as np
import pandas as pd


if __name__ == "__main__":
	with open("day1.txt") as f:
		data = f.read().splitlines()

	# PART 1
	split_list = []
	in_loop = []
	for item in data:
		if item:
			in_loop.append(int(item))
		else:
			split_list.append(in_loop)
			in_loop = []
	print(f"Part1 answer: {max([sum(i) for i in split_list])}")


	sorted_sums = sorted([sum(i) for i in split_list], reverse=True)
	print(sorted_sums[0:3])
	print(f"Part2 answer: {sum(sorted_sums[0:3])}")