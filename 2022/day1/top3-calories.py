#Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
import numpy as np
def top3calories():
	with open('input', 'r') as f:
		#parse input			
		lines = f.read()
		elfs = lines.split("\n\n")
		elfs = [s.replace('\n', ',') for s in elfs]
		#divide list in groups 		
		food=[]		
		for i in range(len(elfs)):		
			food.append(np.fromstring(elfs[i],dtype=int,sep=","))		
		#calculate sum for each group			
		summe=[]		
		for i in range(len(food)):
			summe.append(np.sum(food[i]))				
		#sort the list		
		temp = np.sort(summe)
		#reverse order and save first three entries
		top3 = np.sort(temp)[::-1][0:3]
		#output total calories of top3
		print(np.sum(top3))		
top3calories()
