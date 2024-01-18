
# Camel Case, 

def camelCase(s):
   result = []

   for letter in s:
      if letter == letter.upper():
         DataSplit = s.split(letter)
         result.append(DataSplit)
   

   print(len(DataSplit))

s = str(input())
camelCase(s)
