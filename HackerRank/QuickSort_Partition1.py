
#Quick Sort Partition-1

def quickSort(arr):
    left = []
    equal = []
    right = []
    pivot = arr[0]

    for x in arr:
        if x<pivot:
            left.append(x)
        elif x==pivot:
            equal.append(x)
        elif x>pivot:
            right.append(x)
    
    sumData =left+equal+right
    Data = ''.join(sumData)
    return Data

n = int(input())
arr = list(map(int,input().rstrip().rsplit()))[:n]
print(quickSort(arr))