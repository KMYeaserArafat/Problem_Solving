
# String Construction
# Question Link : https://www.hackerrank.com/challenges/string-construction/problem?isFullScreen=true


def char_to_index(char):
        return ord(char.lower()) - ord('a') + 1

def stringConstruction(s):
    sList = list(s)
    lastChar = sList[len(sList)-1]
    return char_to_index(lastChar)


n = int(input())
for t in range(0,n):
    s = input().rstrip()
    result = stringConstruction(s)
    print(result)
    