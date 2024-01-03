"""
Binary Number count, 

n = how many digit in a string, 
m = how many string 

"""

n,m = map(int,input().split())
topices = [input() for i in range(n)]

result = []
maxpoint = 0
count = 0
point = 0
for x in range(n):
    for y in range(x,n):
        for i,j in zip(topices[x],topices[y]):
            if i=='1' or j=='1':
                point+=1
            
            if point>maxpoint:
                maxpoint=point
                count = 1
            elif point==maxpoint:
                count+=1

print("MaxPoint : ", maxpoint)
print("Count : ", count)
print("point : ", point)

