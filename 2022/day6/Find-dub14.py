#identify the first position where the four most recently received characters were all differentHow many characters need to be processed before the first start-of-packet marker is detected?
def find_dub():	
	with open('input','r') as f:
		s = f.read()
		for i in range(len(s)):		
			q = s[i:i+14]
			x = set(q)
			if len(q) == len(x):
				return s.index(q)+14
print(find_dub())
