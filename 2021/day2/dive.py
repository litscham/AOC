#How many measurements are larger than the previous measurement?
import numpy as np
import re
def endpoint():
	with open('input', 'r') as f:
		lines = f.read()
		values = lines.split("\n")
		directions = [re.split(r'(\d+)', s)[0:2] for s in values]
		for item in directions:
			if item[i] == 'Forward':
				Forward = item[]
endpoint()
