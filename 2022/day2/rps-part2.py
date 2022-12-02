#Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
#A = rock (loose=Scissor, win=paper(2), draw=rock(1))
#B = paper (loose=Rock(1), win=scissor(3), draw=paper(2))
#C = scissor (loose=paper(2), win=rock(1), draw=scissor(3))
import numpy as np
def rpsscore2():
	rock = 1
	paper = 2
	scissor = 3
	#X 
	loose = 0 
	#Y  
	draw = 3 
	#Z 
	win = 6
	score = 0
	with open('input', 'r') as f:
		#parse input			
		lines = f.read()
		lines = lines.split("\n")
		lines = [s.replace(' ', '') for s in lines]
		for i in range(len(lines)-1):
			#need to lose and op has rock
			if lines[i][1] == 'X' and lines[i][0] == 'A':
				score = score + loose + scissor	
			#need to lose and op has paper		
			elif lines[i][1] == 'X' and lines[i][0] == 'B':
				score = score + loose + rock
			#need to lose and op has scissor	
			elif lines[i][1] == 'X' and lines[i][0] =='C':
				score = score + loose + paper
			#need to draw and op has rock
			elif lines[i][1] == 'Y' and lines[i][0] == 'A':
				score = score + draw + rock
			#need to draw and op has paper			
			elif lines[i][1] == 'Y' and lines[i][0] == 'B':
				score = score + draw + paper
			#need to draw and op has scissor
			elif lines[i][1] == 'Y' and lines[i][0] =='C':
				score = score + draw + scissor
			#need to win and op has rock	
			elif lines[i][1] == 'Z' and lines[i][0] == 'A':
				score = score + win + paper
			#need to win and op has paper		
			elif lines[i][1] == 'Z' and lines[i][0] == 'B':
				score = score + win + scissor
			#need to win and op has scissor
			elif lines[i][1] == 'Z' and lines[i][0] =='C':
				score = score + win + rock
		#check how many loses		
		#check how many wins		
		#check how many draws			
		print(score)
rpsscore2()
