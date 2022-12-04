#In how many assignment pairs does one range fully contain the other?
import numpy as np
def overlap():
	with open('input', 'r') as f:
		#parse input			
		lines = f.read().split('\n')[:-1]
		lines = [i.split(',') for i in lines]
		e1 = []
		e2 = []
		for i in range(len(lines)):
			e1.append(lines[i][0].split('-'))
			e2.append(lines[i][1].split('-'))
		summe = 0
		for i in range(len(e1)):
			a = np.arange(int(e1[i][0]),int(e1[i][1])+1)
			b = np.arange(int(e2[i][0]),int(e2[i][1])+1)
			if len(set(a) & set(b)) == 0:
				summe = summe + 1
			else:
				pass	
		print(len(e1)-summe)
overlap()
