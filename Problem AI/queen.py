import random

def createMatrix(n):
    adj=[]
    for i in range(n):
        row=[]
        for j in range(n):
            row.append(0)
        adj.append(row)
    return adj


def printMatrix(M):
    for i in M:
        print(i,end="\n")
    print()



def assignQueen(Q):
    # place queen randomly
    for x in range(4):
        Q[x][random.randint(0,3)] = 1
    return Q


def rowAttack(coordinate, Q):
    row, col = coordinate
    for j in range(len(Q)):
        if Q[row][j] == 1 and j != col:
            return True
    return False

def columnAttack(coordinate, Q):
    row, col = coordinate
    for i in range(len(Q)):
        if Q[i][col] == 1 and i != row:
            return True
    return False

def diagonalAttack(coordinate, Q):
    row, col = coordinate
    for i in range(len(Q)):
        for j in range(len(Q)):
            if (i != row and j != col) and (i + j == row + col or i - j == row - col) and Q[i][j] == 1:
                return True
    return False



def isAttack(Q):

     if rowAttack==True:
         print("Row Attack")
     elif columnAttack==True:
         print("Column Attack")
     elif diagonalAttack==True:
         print("Diagonal Attack")
     else:
         print("Attack in q1 and q2")
         
             
    

Q = createMatrix(4)
printMatrix(Q)
Q=assignQueen(Q)
printMatrix(Q)
isAttack(Q)
