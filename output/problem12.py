
n = int(input())

for x in range(n):
    Data = int(input())
    if(Data>=38 and Data%5>=3):
        while(Data%5 !=0):
            Data = Data+1
    
    print(Data)

