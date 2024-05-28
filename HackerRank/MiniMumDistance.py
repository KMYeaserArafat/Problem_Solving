#Minimum Distance 

from collections import Counter

def MinimumDistance(n,arr):
    Datalist = []
    indexlist = []
    for x in range(n):
        for y in range(x+1,n):
            if(arr[x]==arr[y]):
                Datalist.append(arr[x])

    for i in range(n):
        for j in range(len(Datalist)):
            if(arr[i]==Datalist[j]):
                indexlist.append(i)

    indexlist.sort(reverse=True)

    cal1 = indexlist[0]-indexlist[3]
    cal2 = indexlist[1]-indexlist[2]

    calculationList = [cal1,cal2]
    minimumDistance = min(calculationList)
    
    return minimumDistance



n = int(input())
arr = list(map(int,input().split()))
print(MinimumDistance(n,arr))