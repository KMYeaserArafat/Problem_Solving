

n = int(input("How Much Data Wanto take : "))

DataList = []

for x in range(n):
    TakeData = int(input(f"Enter Data {x} Position : "))
    DataList.append(TakeData)

print(DataList)

for y in range(n):
    if(DataList[y]>=38 and DataList[y]%5>=3):
        if(DataList[y]%5 !=0):
            DataList[y]+=2

print(DataList)