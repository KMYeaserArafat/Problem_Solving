
#sales_by_Match, 

from collections import Counter

n = int(input().rstrip())
arr  = list(map(int,input().split()))
num = 0

for i in range(0,n):
    id = 1
    for j in range(i+1,n):
        if arr[i] == None:
            continue
        if arr[i] == arr[j] and id==1:
            num +=1
            id+=1
            arr[j]= None

print(num)

