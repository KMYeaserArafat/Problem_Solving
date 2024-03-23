
# The Love-Letter Mystery, 


def theLoveLetterMystery(s):
    ans = s[::-1]

    if(s==ans):
        return 0
    else:
        return sum(abs(ord(s[i]) - ord(s[-(i+1)])) for i in range(len(s)//2))


t = int(input())

for x in range(t):
    s = input()
    print(theLoveLetterMystery(s))





