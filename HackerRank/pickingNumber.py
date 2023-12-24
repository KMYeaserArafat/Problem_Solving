from collections import Counter

def pickingNumber(a,n):
    d = Counter(a)
    best = 0
    for i in range(n):
        best =  max(d[i]+d[i-1],best)
    print(best)



n = int(input())
a = list(map(int,input().split()))
pickingNumber(a,n)