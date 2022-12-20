#How many positions does the tail of the rope visit at least once?
def rope():	
    with open('input_test','r') as f:	
        #parse input		
        d = f.read()
        d = d.split("\n")
        d = [i.split(" ") for i in d]
        d = d[:-1]
	idx = {'Hx':0,'Tx':0, 'Hy':0, 'Ty':0}
		if abs(idx['Hx'] - idx['Tx']) == 0 or abs(idx['Hy'] - idx['Ty']) == 0:
    		return idx
print(rope())
