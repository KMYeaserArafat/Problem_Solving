# Counter-Sort-2

def countingSort(arr):
    count = [0]*100
    for index in arr:
        count[index]+=1

    for i in range(100):
        if(count[i]>0):
            print(" ".join([str(i)]*count[i]),end=" ")

n=int(input())
arr = list(map(int,input().split()))[:n]
countingSort(arr)



    