#How many measurements are larger than the previous measurement?
import numpy as np
def diffchecker():
	with open('input', 'r') as f:
		lines = f.read()
		values = lines.split("\n\n")
		values = [s.replace('\n', ',') for s in values]	
		frame=[]		
		for i in range(len(values)):		
			frame.append(np.fromstring(values[i],dtype=int,sep=","))					
		diffs = np.diff(frame)
		print(np.sum(diffs > 0))
diffchecker()
