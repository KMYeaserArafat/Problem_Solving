# Equalize the array, 

from collections import Counter

def equalizeArray(arr,n):

    f = Counter(arr)
    maxCount = max(f.values())
    answer  = n-maxCount
    return answer

n = int(input())
arr = list(map(int,input().split()))
print(equalizeArray(arr,n))