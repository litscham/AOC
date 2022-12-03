#What's the end position
import numpy as np
import re
def endpoint():
	with open('input', 'r') as f:
		lines = f.read()
		values = lines.split("\n")
		directions = [re.split(r'(\d+)', s)[0:2] for s in values]
		forward = 0
		depth = 0
		for i in range(len(directions)-1):
			if directions[i][0] in ['forward']:
				forward = forward + directions[i][1]
			elif directions[i][0] == 'down':
				depth = depth + directions[i][1]
			elif directions[i][0] == 'up':
				depth = depth - directions[i][1]
		print(forward)
endpoint()
