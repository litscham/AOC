#lines 0-6 are creates
#line 7 is index of creates
#lines 7: are instructions 'move #creates from source index to destination index 
#index 0 = number of creates, 1 = destination, 2 = source 
#move_create = creates.pop(instructions[0])[-1]
import numpy as np
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
with open('input','r') as f:
    instructions = f.readlines()[10:]
    instructions = [s.replace("move ","").replace("from ","").replace("to ", "").replace("\n","").split(' ') for s in instructions]
    for i in np.arange(len(instructions)):
	j = int(instructions[i][0])
        #print(j, creates.get(int(instructions[i][1]))[-j:])
	creates[int(instructions[i][2])] += creates.get(int(instructions[i][1]))[-j:]
        creates.update({int(instructions[i][1]): creates.pop(int(instructions[i][1]))[:-j]})
for key in creates.keys():
	print(creates.get(key)[-1])


