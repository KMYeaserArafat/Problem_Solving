#Sharlok and square, 

import math


t = int(input())

for x in range(t):
    count = 0
    a,b= map(int,input().split())
    
    sNum = int(math.ceil(math.sqrt(a)))
    eNum = int(math.floor(math.sqrt(b)))

    if(sNum<eNum):
        result = eNum-sNum+1
        print(result)
    else:
        print(0)









