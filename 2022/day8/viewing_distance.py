#highest scenic score
def viewing_distance():	
    with open('input','r') as f:	
        #parse input		
        s = f.read()
        s = s.split("\n")
        m = []		
        for i in range(len(s)):
            m.append(list(s[i]))	
        m = m[:-1]
        curr = 0
        scores = {}
        for i in range(len(m)):
            print("i=%d" %i)
            for j in range (len(m)):
                n = 1
                score_right = 0
                score_left = 0
                score_up = 0
                score_down = 0
                print("j=%d" % j)
                curr = int(m[i][j])
                print("current is %d " % curr)
                #right
                print("Right")
                while n+j <= len(m)-1:
                    print("n=%d " % n)
                    print("j+n=%d " % (j+n))
                    if curr > int(m[i][j+n]):
                            score_right = score_right+1
                            n = n + 1
                            print("yes!")
                    elif curr == int(m[i][j+n]):
                        score_right = score_right+1
                        print("yes equal!")
                        break
                    else:
                        print("no")
                        score_right = score_right+1
                        break
                #left
                print("left")
                n = 1
                while j-n >= 0:
                    print("n=%d " % n)
                    print("j-n=%d " % (j-n))
                    if curr > int(m[i][j-n]):
                        score_left = score_left+1
                        n = n + 1
                        print("yes!")
                    elif curr == int(m[i][j-n]):
                        score_left = score_left+1
                        print("yes equal!")
                        break
                    else:
                        print("no")
                        score_left = score_left+1
                        break
                n=1
                #down
                print("down")
                while i+n <= len(m)-1:
                    print("n=%d " % n)
                    print("i+n=%d " % (i+n))
                    if curr > int(m[i+n][j]):
                        score_down = score_down+1
                        n = n + 1
                        print("yes!")
                    elif curr == int(m[i+n][j]):
                        score_down = score_down+1
                        print("yes equal!")
                        break
                    else:
                        print("no")
                        score_down = score_down+1
                        break
                #up
                n = 1
                print("up")
                while i-n >= 0:
                    print("n=%d " % n)
                    print("i-n=%d " % (i-n))
                    if curr > int(m[i-n][j]):
                        score_up = score_up+1
                        n = n + 1
                        print("yes!")
                    elif curr == int(m[i-n][j]):
                        score_up = score_up+1
                        print("yes equal!")
                        break
                    else:
                        print("no")
                        score_up = score_up+1
                        break
                scores.update({(i,j) : (score_right, score_left, score_down, score_up)})
        #print(max(scores, key=scores.get),max(scores.values()))
        #print(type(scores[(0,0)]))
        tmp = list(scores.values())
        scs = []
        for i in range(len(tmp)):
            scs.append(tmp[i][0]*tmp[i][1]*tmp[i][2]*tmp[i][3])
        return max(scs)
print(viewing_distance())
