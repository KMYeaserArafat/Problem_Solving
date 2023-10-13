'''
2.	Read 100 numbers from file (random-int.txt) and stores them in array 
and randomly selects 10 elements from that array and sums them up, print the sum.

'''

import numpy
import matplotlib.pyplot as pplot


def ProcessData(fileName):
    
    #Read Data into a .txt file, 
    file = open(fileName,"r")
    Data = file.read()
    file.close()

    return Data


PData = ProcessData("problem6_1_IntNum.txt").split(",")
print("All Data : ", PData,"\n")

DataList = []

for x in range(len(PData)):
    DataList.append(x)

RandomNumber = numpy.random.choice(DataList,10)
print("Random Number : ", numpy.array(RandomNumber))
Rsum = sum(RandomNumber)
print("Sum of Random Number : ", Rsum)


# Show Bar, 
pplot.bar(RandomNumber,Rsum)
pplot.show()






