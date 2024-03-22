
# Find the Median, 

def findMedian(arr):
    arr.sort()
    meanValue = arr[len(arr)//2]
    return meanValue



n = int(input())
arr = list(map(int,input().split()))[:n]

print(findMedian(arr))
