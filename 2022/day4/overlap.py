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
			print(len(set(a) & set(b)) , len(set(a)) ,len(set(b)))
			if len(set(a) & set(b)) == len(set(a)):
				summe = summe + 1
			elif len(set(a) & set(b)) == len(set(b)):
				summe = summe + 1
			else:
				pass
		#start e1[i][0] end e1[i][1]
		#check if len() from set(a) & set(b) == set(a) or set(a) & set(b) == set(b)		
		'''del(lines[-1])				
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
			summe = summe +	prio_dict[common[i]]'''		
		print(summe)
overlap()
