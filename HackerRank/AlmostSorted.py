
# Almost Sorted 

def AlmostSorted(arr,n):
    for x in range(0,n):
        for y in range(x+1, n):
            if arr[x]<arr[y]:
                return "YES"
            else:
               return "NO"


n = int(input())
arr = list(map(int,input().strip().split()))[:n]
print(AlmostSorted(arr,n))
