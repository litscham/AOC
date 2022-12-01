#how much calories does the elf with the most calories have
import numpy as np
def mostcalories():
	with open('input', 'r') as f:
		lines = f.read()
		elfs = lines.split("\n\n")
		elfs = [s.replace('\n', ',') for s in elfs]
		food=[]		
		for i in range(len(elfs)):		
			food.append(np.fromstring(elfs[i],dtype=int,sep=","))					
		summe=[]		
		for i in range(len(food)):
			summe.append(np.sum(food[i]))		
		print(np.max(summe))
mostcalories()
