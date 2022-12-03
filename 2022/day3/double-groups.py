#Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
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
		lines = [lines[x:x+3] for x in range(0, len(lines),3)]
		common = []		
		for i in range(len(lines)-1):
			common.append(list(set(lines[i][0]) & set(lines[i][1]) & set(lines[i][2])))
		common=sum(common,[])
		summe = 0		
		for i in range(len(common)):
			summe = summe +	prio_dict[common[i]]		
		print(summe)	

double()
