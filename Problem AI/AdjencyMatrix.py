


def AdjencyMatrix(size):
    adj = []
    for x in range(size):
        row = []
        for y in range(size):
            Data = int(input())
            row.append(Data)
        adj.append(row)

    return adj


def printMatrix(size):
    for i in size:
        print(i, end="\n")



n = int(input("Declear the Adjency Size : "))
Q = AdjencyMatrix(n)
printMatrix(Q)
