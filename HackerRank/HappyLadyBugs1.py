
from collections import Counter

g = int(input())
for t in range(g):
    n = int(input())
    b = input()

    Data = ''

    for a in range(len(b)):
        for c in b:
            if c=="_":
                Data = b[a-1]

                if Counter(Data)==Counter("_"):
                    print("YES")
                else:
                    print("NO")
