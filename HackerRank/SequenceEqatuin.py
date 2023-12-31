#Sequence-Equation, 


n = int(input())
p = list(map(int,input().split()))

for x in range(1,n+1):
    if(x in p):
        indexNum1 = p.index(x)+1
        if(indexNum1 in p):
            indexnum2 = p.index(indexNum1)+1
            print(indexnum2)



