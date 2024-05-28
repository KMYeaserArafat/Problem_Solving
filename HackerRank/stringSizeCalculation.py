

def function1(sizeArray,DataSize,DataList):
    cal1 = sizeArray*DataSize
    lenOfArr = len(DataList)

    Data = 0
    for x in range(lenOfArr):
        Data = len(DataList[x])
    
    cal2 = Data*lenOfArr

    if cal1==cal2:
        return cal2
    else:
        return 'Not Same'


sizeArray = int(input())
DataSize = int(input())
DataList = [input() for x in range(sizeArray)]
print(function1(sizeArray,DataSize,DataList))




