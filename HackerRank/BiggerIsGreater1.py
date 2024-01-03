import string


t = int(input())

SortedDataStore = []

for x in range(t):
    Data = input()
    DataList1 = list(Data)
    DataList1.sort(reverse=True)
    sortDataStr = ''
    for x in DataList1:
        sortDataStr+=x
    SortedDataStore.append(sortDataStr)


for y in range(t):
    print(SortedDataStore[y])



    

    



