# Modified Kaprekar Numbers

n = int(input())
d = int(input())

nSquare = str(n**2)
lenSquare = len(nSquare)

nDataList = [nSquare[i:i+d] for i in range(0,lenSquare,d)]

print(nDataList)
sum = 0
for x in range(len(nDataList)):
    Data = int(nDataList[x])
    sum+=Data


if(sum==n):
    print("Correct")
else:
    print("Incorrect")




