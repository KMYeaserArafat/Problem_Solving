"""
Nural Network Build it Base on photo 1, 

"""

import math

def InsertIData(n,arr,ValueType):
    for x in range(n):
        insertValue = input(f"Insert Value {ValueType},Index: {x+1}: ")
        arr.append(float(insertValue))

def MultipleCal(arr1,arr2,n):
    x = 0.0
    for x in range(n):
        x+=arr1[x]*arr2[x]
    return x
        
def checkFunction(xValues):
    f = 1/1+math.exp(-xValues)
    return f

def AllWorkMethod(i,B,n,BValues):
    InsertIData(n,B,BValues)
    x = MultipleCal(i,B,n)
    h = checkFunction(x)
    return h



#here atfirst take value how many node in first Layer, 
n = int(input("How Many first Layer input values (i): "))
#here the the node values(i),
i= []
InsertIData(n,i,"i",)


#here start work Layout 2, 
B1 = []
c1 = int(input("How Many number Connected in h1 : "))
h1 = AllWorkMethod(i,B1,c1,"B1")

B2 = []
c2 = int(input("How Many number Connected in h2 : "))
h2 = AllWorkMethod(i,B2,c2,"B2")

B3 = []
c3 = int(input("How Many number Connected in h3 : "))
h3 = AllWorkMethod(i,B3,c3,"B3")

#Here Start work for 3rd layer, 
i2 = [h1,h2,h3]
B4 = []
Olc = int(input("How Many number Connected in Ol : "))
ol = AllWorkMethod(i2,B4,Olc,"B4")

print("3rd Layout OL : ", ol)









