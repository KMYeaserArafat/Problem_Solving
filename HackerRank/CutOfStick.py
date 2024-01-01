from collections import Counter

def CutTheStick(arr):
    result = []
    n = len(arr)
    s = Counter(arr)

    for x in sorted(s.keys()):
        result.append(n)
        n-=s[x]

    for y in range(len(result)):
        print(result[y])

n = int(input())
arr = list(map(int,input().split()))
CutTheStick(arr)


