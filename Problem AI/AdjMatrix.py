import random

#create matrix, 
def createMatrix(size):
    adj = []
    for x in range(size):
        row = []
        for y in range(size):
            Data = random.randint(0,7)
            row.append(Data)
        adj.append(row)
    
    return adj

#Print matrix, 
def printMatrix(size):
    for i in size:
        print(i,end="\n")



Q = createMatrix(4)
printMatrix(Q)