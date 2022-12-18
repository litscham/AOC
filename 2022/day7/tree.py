#Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
def tree():	
	with open('input','r') as f:
		s = f.read()
		s = s.split('\n')
		if s[i].startswith("cd "):
			s[i].split(" ")
		#s = [i.split('') for i in s]
		return s
print(tree())
