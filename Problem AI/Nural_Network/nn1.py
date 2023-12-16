'''
It's making for photo1,

'''
import math


def function1(Data):
    g = float(1/1+math.exp(-Data))
    return g



#layer1, 
#In the layout1 already has i1, i2, i3, i4;
i = []
w = []

for x in range(4):
    insertLayer1iValue = int(input(f"Insert i{x+1} Value : "))
    i.append(insertLayer1iValue)
print("i : ", i)


#insert value for h1, 
B1 = []
for x in range(4):
    insertB1Value = float(input(f"Enter B1 Value in index {x} : "))
    B1.append(insertB1Value)



#insert value for h2, 
B2 = []
for x in range(4):
    insertB2Value = float(input(f"Enter B2 Value in index {x} : "))
    B2.append(insertB2Value)


#insert value for h3, 
B3 = []
for x in range(4):
    insertB3Value = float(input(f"Enter B3 Value in index {x} : "))
    B3.append(insertB3Value)

#insert value for h3, 
B4 = []
for x in range(4):
    insertB4Value = float(input(f"Enter B4 Value in index {x} : "))
    B4.append(insertB4Value)


print(B1)
print(B2)
print(B3)
print(B4)

x1 = 0.0
x2 = 0.0
x3 = 0.0
x4 = 0.0

for x in range(4):
    x1 +=float(i[x])*float(x1[x])

for y in range(4):
    x2 += float(i[y])*float(x2[y])

for z in range(4):
    x3 +=float(i[z])*float(x3[z])

for j in range(4):
    x4 +=float(i[j])*float(x4[j])

h1 = function1(x1)
h2 = function1(x2)
h3 = function1(x3)
h4 = function1(x4)

h = [h1,h2,h3,h4]

B5 = []
for x in range(3):
    insertB5Value = float(input(f"Enter B5 Value in index {x} : "))
    B5.append(insertB5Value)

x5 = 0.0

for i in range(3):
    x5 += float(h[i])*B5[i]

ol = function1(x5)






