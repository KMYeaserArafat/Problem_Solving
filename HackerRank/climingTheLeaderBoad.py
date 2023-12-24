#Climbing the leaderboard, 

from collections import Counter
from bisect import bisect_left
        

r = int(input())
ranking = list(map(int,input().split()))

p = int(input())
player = list(map(int,input().split()))

counts = Counter(ranking)
counts = sorted(counts)

n = len(counts)

for x in player:
    i = bisect_left(counts,x)
    if(i<n and counts[i]==x):
        print(n-i)
    else:
        print(n+1-i)

