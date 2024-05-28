# Insertion Sort Advanced Analysis


def InsertionSort():
    count = 0
    temp = 0
    for x in range(0,len(arr)):
        for y in range(x,len(arr)):
            if(arr[x]>arr[y]):
                temp=arr[x]
                arr[x]=arr[y]
                arr[y]=temp
                count+=1
    return count



t = int(input())
for r in range(t):
    n = int(input())
    arr = list(map(int,input().split()))[:n]
    print(InsertionSort())