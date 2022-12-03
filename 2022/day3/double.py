#Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
import numpy as np
def double():
	char = []
	prio = np.arange(1,53,dtype=int)
	for i in range(ord('a'), ord('z')+1):
		char.append(chr(i))	
	for i in range(ord('A'), ord('Z')+1):
		char.append(chr(i))
	prio_dict = dict(zip(char, prio))
	with open('input', 'r') as f:
		#parse input			
		lines = f.read()
		lines = lines.split("\n")
		del(lines[-1])				
		first = []
		second = []
		for e in range(len(lines)):
			first.append(lines[e][0:int(len(lines[e])/2)])
			second.append(lines[e][int(len(lines[e])/2):])
		comp1 = []
		comp2 = []
		for i in range(len(first)):
			comp1.append(list(first[i]))
			comp2.append(list(second[i]))
		common = []
		for i in range(len(comp1)):
			common.append(list(set(comp1[i]) & set(comp2[i])))
		common=sum(common,[])
		summe = 0		
		for i in range(len(common)):
			summe = summe +	prio_dict[common[i]]	
		print(summe)	

double()
