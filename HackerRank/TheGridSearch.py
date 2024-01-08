
#The-Grid-Search, 


DataStore1 = []
DataStore2 = []

t = int(input())
for n in range(t):
    r,c = map(int,input().split())
    for i in range(r):
        Data1 = input()
        DataStore1.append(Data1)

    r1,c1 = map(int,input().split())
    for j in range(r1):
        Data2 = input()
        DataStore2.append(Data2)

    for a in range(r):
        for b in range(r1):
            if DataStore2[b] in DataStore1[a]:
                print("Yes")
            else:
                print("No")






    
    




