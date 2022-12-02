#What would your total score be if everything goes exactly according to your strategy guide?
#A & X = Rock = 1 Point
#B & Y = Paper = 2 Point
#C & Z = Scissor = 3 Point
#Win = 6 Points
#Draw = 3 Points
#Loose = 0 Point
import numpy as np
def rpsscore():
	score = 0
	with open('input', 'r') as f:
		#parse input			
		lines = f.read()
		lines = lines.split("\n")
		lines = [s.replace(' ', '') for s in lines]
		#check what I chose
		for i in range(len(lines)-1):
			if lines[i][1] == 'X' and lines[i][0] == 'A':
				score = score + 1 + 3			
			elif lines[i][1] == 'X' and lines[i][0] == 'B':
				score = score + 1 + 0
			elif lines[i][1] == 'X' and lines[i][0] =='C':
				score = score + 1 + 6
			elif lines[i][1] == 'Y' and lines[i][0] == 'A':
				score = score + 2 + 6			
			elif lines[i][1] == 'Y' and lines[i][0] == 'B':
				score = score + 2 + 3
			elif lines[i][1] == 'Y' and lines[i][0] =='C':
				score = score + 2 + 0	
			elif lines[i][1] == 'Z' and lines[i][0] == 'A':
				score = score + 3 + 0			
			elif lines[i][1] == 'Z' and lines[i][0] == 'B':
				score = score + 3 + 6
			elif lines[i][1] == 'Z' and lines[i][0] =='C':
				score = score + 3 + 3	
		#check how many loses		
		#check how many wins		
		#check how many draws			
		print(score)
rpsscore()
