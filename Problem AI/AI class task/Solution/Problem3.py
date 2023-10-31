'''
3.	A die was rolled 100 times and saved each outcome in a text file (dice.txt) 
    and calculates the frequency and probability of each outcome. 
    (Rolling one die by choosing one of the integers 1, 2, 3, 4, 5, or 6 at random).
'''
import numpy
import matplotlib.pyplot as ppolot

def dice(rollTime):
    DiceData = []
    frequency = {}

    for Data in range(rollTime):
        DiceData.append(numpy.random.randint(6)+1)

    for iteams in DiceData:
        frequency[iteams] = frequency.get(iteams,0)+1
    
    return sorted(frequency.items(),key=lambda x: x[0], reverse=False)
    


rollTime = 100
all = dice(rollTime)
print(all)

x = []
y = []

for i in all:
    x.append(i[0])
    y.append(i[1])


ppolot.bar(x,y)
ppolot.grid()
ppolot.show()