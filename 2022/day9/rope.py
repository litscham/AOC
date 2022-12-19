#How many positions does the tail of the rope visit at least once?
def rope():	
    with open('input_test','r') as f:	
        #parse input		
        d = f.read()
        d = d.split("\n")
        d = [i.split(" ") for i in d]
        d = d[:-1]
    idx = {'Hx':0,'Tx':0, 'Hy':0, 'Ty':0}
    c = set()
    for i in range(len(d)):
        nH = 1
        nT = 1
        if d[i][0] == 'R':
            print("right " + str(d[i][1]))
            while nH <= int(d[i][1]):
                print(nH)
                idx['Hx'] += 1
                nH = nH + 1
                c.add((idx['Tx'],idx['Ty']))
                if idx['Hx'] != idx['Tx']-1:
                    idx['Tx'] += 1
                    nT += 1
                print(idx)
        elif d[i][0] == 'L':
            print("left "+ str(d[i][1]))
            while nH <= int(d[i][1]):
                print(nH)
                idx['Hx'] -= 1
                nH = nH + 1
                c.add((idx['Tx'],idx['Ty']))
                idx['Tx'] -= 1
                nT += 1
        elif d[i][0] == 'U':
            print("up "+ str(d[i][1]))
            while nH <= int(d[i][1]):
                print(nH)
                idx['Hy'] += 1
                nH = nH + 1
                c.add((idx['Tx'],idx['Ty']))
                idx['Ty'] += 1
                #nT += 1
        elif d[i][0] == 'D':
            print("down "+ str(d[i][1]))
            while nH <= int(d[i][1]):
                print(nH)
                idx['Hy'] -= 1
                nH = nH + 1
                c.add((idx['Tx'],idx['Ty']))
                idx['Ty'] -= 1
                nT += 1
    return len(c)
print(rope())
