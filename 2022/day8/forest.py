#how many trees are visible from outside the grid?
def forest():	
	with open('input','r') as f:	
		#parse input		
		s = f.read()
		s = s.split("\n")
		m = []		
		for i in range(len(s)):
			m.append(list(s[i]))	
		m = m[:-1]
		idx = set()
		#edge		
		for i in range(len(m)):
			for j in range(len(m)):			
				if i == 0 or j == 0:
					idx.add((i, j))	
				elif i == len(m)-1 or j == len(m)-1:
					idx.add((i, j))	
		#interior
		print("left to right")
		for i in range(1,len(m)):
			print("i=%d" %i)
			curr = int(m[i][0])
			print("current is %d " % curr)
			for j in range(1,len(m)):
				print("j=%d" % j)
				if curr < int(m[i][j]):
					curr = int(m[i][j])
					idx.add((i, j))
					print("added")
					print("current is %d " % curr)
		print("down")
		for j in range(1,len(m)):
			print("j=%d" %j)
			curr = int(m[0][j])
			print("current is %d " % curr)
			for i in range(1,len(m)):
				print("i=%d" % i)
				if curr < int(m[i][j]):
					curr = int(m[i][j])
					idx.add((i, j))
					print("added")
					print("current is %d " % curr)
		print("right to left")
		for i in range(1,len(m)-1,1):
			print("i=%d" %i)
			curr = int(m[i][len(m)-1])
			print("current is %d " % curr)
			for j in range(len(m)-2,-1,-1):
				print("j=%d" % j)
				if curr < int(m[i][j]):
					curr = int(m[i][j])
					idx.add((i, j))
					print("added")
					print("current is %d " % curr)
		print("up")
		for j in range(1,len(m)):
			print("j=%d" %j)
			curr = int(m[len(m)-1][j])
			print("current is %d " % curr)
			for i in range(len(m)-1,0,-1):
				print("i=%d" % i)
				if curr < int(m[i][j]):
					curr = int(m[i][j])
					idx.add((i, j))
					print("added")
					print("current is %d " % curr)
		return len(idx)
print(forest())
