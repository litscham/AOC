#lines 0-6 are creates
#line 7 is index of creates
#lines 7: are instructions 'move #creates from source index to destination index 

#move_create = creates.pop(instructions[0])[-1]
creates = {	1:'RPCDBG',
		2:'HVG',
		3:'NSQDJPM',
		4:'PSLGDCNM',
		5:'JBNCPFLS',
		6:'QBDZVGTS',
		7:'BZMHFTQ',
		8:'CMDBF',
		9:'FCQG'		
	}
with open('input','r') as instructions:
	print(instructions.readlines().pop(0))#.split("\n")#.replace("move","from","to")#
'''data = open("input", "r").read().replace("-",",").split("\n")
total = 0
for i in data:
    p1, p2, p3, p4 = map(int, i.split(","))
    
    if p1 >= p3 and p2 <= p4: total += 1 #left inside right
    elif p1 <= p3 and p2 >= p4: total += 1 #right inside left
'''
	
