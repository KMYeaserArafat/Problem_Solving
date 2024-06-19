
# # Making Anagrams,
# # Question Link : https://www.hackerrank.com/challenges/making-anagrams/problem?isFullScreen=true
from collections import Counter

def MakingAnagrams(s1,s2):
    d1 = Counter(s1)
    d2 = Counter(s2)

    result = sum(((d1-d2)+(d2-d1)).values())
    return result



s1 = input()
s2 = input()
result = MakingAnagrams(s1,s2)
print(result)










