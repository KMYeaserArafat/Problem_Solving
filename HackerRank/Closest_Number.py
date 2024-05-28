
# Closest Number, 


def closestNumbers(arr):
    ans = []
    m = float('inf')  #make infinity

    for i in range(len(arr)-1):
        m = min(arr[i+1]-arr[i],m)

    for i in range(len(arr)-1):
        if(arr[i+1]-arr[i])==m:
            ans.append(arr[i])
            ans.append(arr[i+1])

    return ans
   
        

n = int(input())
arr = list(map(int,input().split()))[:n]
arr.sort()

print(closestNumbers(arr))
