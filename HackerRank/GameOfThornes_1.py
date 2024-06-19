# Game of  Thrones - 1
# Question Link : https://www.hackerrank.com/challenges/game-of-thrones/problem?isFullScreen=true

from collections import Counter

def gameOfThrones(s):
    
    s1 = list(Counter(s).values())
    for x in range(len(s1)):
        if(s1[x]==1 or s1[x]<1):
            return "NO"
        else:
            return "YES"



s = input()
result =  gameOfThrones(s)
print(result)
