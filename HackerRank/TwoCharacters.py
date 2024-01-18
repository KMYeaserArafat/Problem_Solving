
from collections import Counter


def TwoCharacters(s):
   frq = Counter(s)
   maxChar = max(frq, key=frq.get)
   maxfrqValue = max(frq.values())
   minChar = min(frq, key=frq.get)
   minfrqValue = min(frq.values())

   if maxChar in s:
      newData = s.replace(maxChar,"")
   if minChar in s:
      result = newData.replace(minChar,"")
    
   print(result)
  
lenghtOfs = int(input())
s = str(input())[:lenghtOfs]
TwoCharacters(s)


