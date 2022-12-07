import pandas as pd
import numpy as np
from collections import defaultdict

# Define navigation functions
def cd(current_path, cd_path):
	if cd_path == '..':
		current_path.pop()

	else:
		current_path.append(cd_path)

	return current_path

def ls(file_list):
	size = 0
	for item in file_list:
		if item[0] == 'dir':
			pass
		else:
			size += int(item[0])
	return size

if __name__ == "__main__":
	with open("day7.txt") as f:
		data = f.read().splitlines()

	# Store size as int for each path iteratively
	size_dict = defaultdict(int)

	# Holds current Path
	current_path = []
	
	for ind, line in enumerate(data):
		if line[0] == '$':
			command = line.split(' ')
			
			if command[1] == 'cd':
				current_path = cd(current_path, command[2])
			
			elif command[1] == 'ls':
				dir_list = []
				cont = True
				next_line = 1
				while cont:
					file = data[ind+next_line]
					if file[0] == '$':
						cont=False
					else:
						dir_list.append(tuple(file.split(' ')))
						if ind+next_line == len(data)-1:
							cont=False
						else:
							next_line+=1
				size = ls(dir_list)
				for item in range(len(current_path)):
					if item == 0:
						size_dict['/']+=size
					else:
						size_dict['/' + '/'.join(current_path[1:item+1])]+=size
					


		else:
			pass

	total_size_p1=0
	for key, val in size_dict.items():
		if val <= 100000:
			total_size_p1+=val

	print(f"Total Size P1: {total_size_p1}")
	
	filespace = 70000000
	free_space = filespace - size_dict['/']
	needed_space = 30000000 - free_space
	print(f"Total Size P2: {min([i for i in size_dict.values() if i>=needed_space])}")


