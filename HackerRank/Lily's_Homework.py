
# Lily's Homework, 
# Question Link : https://www.hackerrank.com/challenges/lilys-homework/problem?isFullScreen=true



def lilysHomework(arr):
    swapCount = 0

    for a in range(0,len(arr)):
        for b in range(a,len(arr)):
            if(arr[a]<arr[b]):
                temp = arr[a]
                arr[a] = arr[b]
                arr[b] = temp
                swapCount+=1
    
    return swapCount



n = int(input())
arr = list(map(int,input().split()))[:n]
result = lilysHomework(arr)
print(result)

