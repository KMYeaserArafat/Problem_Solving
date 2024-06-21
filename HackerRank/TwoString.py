
# Two String, 
# Question Link : https://www.hackerrank.com/challenges/two-strings/problem?isFullScreen=true


def twoStrings(s1,s2):
    count = 0
    s1List = list(s1)
    for x in range(0,len(s1List)):
        if(s1List[x] in s2):
            count+=1
        else:
            count+=0

    if count >=1:
        return "YES"
    else:
        return "NO"

p = int(input())
for t in range(0,p):
    s1 = input()
    s2 = input()
    result = twoStrings(s1,s2)
    print(result)