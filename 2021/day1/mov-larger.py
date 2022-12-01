#Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?
import numpy as np
def diffchecker():
	with open('input', 'r') as f:
		lines = f.read()
		values = lines.split("\n\n")
		values = [s.replace('\n', ',') for s in values]	
		frame=[]		
		for i in range(len(values)):		
			frame.append(np.fromstring(values[i],dtype=int,sep=","))
		frame=np.reshape(frame, np.size(frame))	
		conv=np.convolve(frame,np.ones(3,dtype=int),'valid')
		diffs = np.diff(conv)		
		print(np.sum(diffs > 0))				
diffchecker()
