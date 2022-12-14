import pandas as pd
import numpy as np
from tqdm import tqdm

if __name__ == "__main__":
	with open("day8.txt") as f:
		data = f.read().splitlines()

	data_store = np.zeros((len(data), len(data[0])))
	for ind, item in enumerate(data):
		row = [int(i) for i in item]
		data_store[ind] = row

	locs = set()
	viewed_trees = 0
	for row_ind, row in enumerate(data_store):
		running_max = -1
		for col_ind, tree in enumerate(row):
			if tree > running_max:
				running_max = tree
				if (row_ind, col_ind) not in locs:
					viewed_trees+=1
					locs.add((row_ind, col_ind))
		running_max=-1
		for col_ind, tree in enumerate(row[::-1]):
			col_ind = len(row)-col_ind-1
			if tree > running_max:
				running_max = tree
				if (row_ind, col_ind) not in locs:
					viewed_trees+=1
					locs.add((row_ind, col_ind))

	for row_ind, row in enumerate(data_store.T):
		running_max = -1
		for col_ind, tree in enumerate(row):
			if tree > running_max:
				running_max = tree
				if (col_ind, row_ind) not in locs:
					viewed_trees+=1
					locs.add((col_ind, row_ind))
		running_max = -1
		for col_ind, tree in enumerate(row[::-1]):
			col_ind = len(row)-col_ind-1
			if tree > running_max:
				running_max = tree
				if (col_ind, row_ind) not in locs:
					viewed_trees+=1
					locs.add((col_ind, row_ind))

	print(viewed_trees)
	view_store = np.zeros((len(data), len(data[0])))

	for row_ind, row in enumerate(data_store):
		for col_ind, col in enumerate(row):
			number_seen = [0,0,0,0]
			#left
			left_buffer = 1
			stop_looking = True
			while col_ind - left_buffer >= 0 and stop_looking:
				if data_store[row_ind, col_ind-left_buffer] < col:
					number_seen[0]+=1
					left_buffer+=1
				else:
					number_seen[0]+=1
					stop_looking=False

			#right
			right_buffer = 1
			stop_looking = True
			while col_ind + right_buffer <= len(row)-1 and stop_looking:
				if data_store[row_ind, col_ind+right_buffer] < col:
					number_seen[1]+=1
					right_buffer+=1
				else:
					number_seen[1]+=1
					stop_looking=False

			#up
			up_buffer = 1
			stop_looking = True
			while row_ind - up_buffer >= 0 and stop_looking:
				if data_store[row_ind-up_buffer, col_ind] < col:
					number_seen[2]+=1
					up_buffer+=1
				else:
					number_seen[2]+=1
					stop_looking=False

			#down
			down_buffer = 1
			stop_looking = True
			while row_ind + down_buffer <= len(data_store)-1 and stop_looking:
				if data_store[row_ind+down_buffer, col_ind] < col:
					number_seen[3]+=1
					down_buffer+=1
				else:
					number_seen[3]+=1
					stop_looking=False
			score = np.prod(number_seen)
			view_store[row_ind,col_ind] = score

	print(view_store)
	print(np.max(view_store))
			



