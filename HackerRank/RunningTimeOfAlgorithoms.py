
#Running Time of Algorithom, 

def runningTime(arr,n):
    count = 0

    for x in range(0,n):
        for y in range(x+1,n):
            if(arr[x]>arr[y]):
                count+=1
                temp  = arr[x]
                arr[x] = arr[y]
                arr[y] = temp

    return count


n = int(input())
arr = list(map(int,input().rstrip().split()))[:n]
print(runningTime(arr,n))

