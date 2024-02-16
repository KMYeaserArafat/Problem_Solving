
#GemStones, 

def gemstones(arr):
    result = set(arr[0])

    for x in range(1,n):
        temp = set(arr[x])
        result = result.intersection(temp)

    return len(result)
   

n = int(input())
arr = list(map(str,input().lower().split()))[:n]
print(gemstones(arr))