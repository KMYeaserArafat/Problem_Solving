"""
/*

Diagonal Difference, 

Input: 
------------
size : 3 (user Input)
11 2 4
4 5 6
10 8 -12

Process 1: 
-------------
11
   5
    -12

(11+5+(-12)) = 4

Process 2: 
--------------

       4
     5
  10
(4+5+10) = 19 
---------------------------------
Digonal Difference = 4-19 = -15

*/

"""

size = 3

X = []
Y = []
Z = []

print("Input 3 Value of X : ")
for x in range(size):
    XData = int(input())
    X.append(XData)

print("Input 3 Value of Y : ")
for y in range(size):
    YData = int(input())
    Y.append(YData)

print("Input 3 Value of Z : ")
for z in range(size):
    ZData = int(input())
    Z.append(ZData)


print("Show X : ", X)
print("Show Y : ", Y)
print("Show Z : ", Z)

D1 = X[0]+ Y[1]+ Z[2]
D2 = X[2]+ Y[1]+ Z[0]

Difference = D1-D2
print("Diagonal Different : ", Difference)





