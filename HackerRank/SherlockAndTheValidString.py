
# Sherlock and the Valid String
# Question Link: https://www.hackerrank.com/challenges/sherlock-and-valid-string/problem?isFullScreen=true

from collections import Counter

def isValid(s):
    sCounter = Counter(s)
    sList = list(sCounter.values())

    count = []

    for x in range(0,len(sList)):
        if sList[x]<=2:
            count.append(1)
        else:
            count.append(0)

    if sum(count)==len(sList):
        return "YES"
    else:
        return "NO"

    

s = input()
result = isValid(s)
print(result)