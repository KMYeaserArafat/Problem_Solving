# Larry's Array

def larryArray(A):
    s = 0

    for i in range(0,len(A)):
        for j in range(i+1, len(A)):
            if A[i]>A[j]:
                s+=1
            
    if s%2==0:
        return "YES"
    else:
        return "NO"




t = int(input())
for x in range(t):
    n = int(input())
    A = list(map(int,input().strip().split()))[:n]
    print(larryArray(A))
