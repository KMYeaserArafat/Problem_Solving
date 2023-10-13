'''
Thow a dice 100 time and find out Frequency(One number how much time) 
'''

import numpy as np
import matplotlib.pyplot as pplot

def DiceRoll(rolltime):
    Datalist = []
    fequency = {}
    for x in range(rolltime):
        Datalist.append(np.random.randint(6)+1)

    for iteams in Datalist:
        fequency[iteams] = fequency.get(iteams,0)+1

    
    return sorted(fequency.items(),key=lambda x: x[0], reverse=False)


all = DiceRoll(100)
print(all)
x=[]
y=[]
for i in all:
    x.append(i[0])
    y.append(i[1])

pplot.bar(x,y)
pplot.grid()
pplot.show()
