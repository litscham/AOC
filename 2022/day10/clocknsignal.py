#find the signal strength during the 20th, 60th, 100th, 140th, 180th, and 220th cycles. What is the sum of these six signal strengths?
cycle = 0
signal = 0
If instruction[:3] in instructions is "addx":
    cycle += 1
    cycle += 1
    signal += instruction[4:]

Else:
    cycle += 1
return
