# Insertion-Sort

def InsertionSort(arr):
    sizeofArr = len(arr)

    for x in range(0,sizeofArr):
        for y in range(x+1, sizeofArr):
            if(arr[x]>arr[y]):
                temp =  arr[x]
                arr[x]= arr[y]
                arr[y]= temp
    
    Data = ' '.join(arr)

    return Data

n = int(input())
arr = list(map(str,input().rstrip().split()))[:n]
Data = InsertionSort(arr)
print(Data)
