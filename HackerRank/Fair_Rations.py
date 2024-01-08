

def fairRations(n,b):
    breads = 0
    
    for x in range(n-1):
        if(b[x]%2==1):
            breads+=2
            b[x+1]+=1

    if b[n-1]%2==1:
        return "No"
    else:
        return breads



n = int(input())
b = list(map(int,input().split()))
print(fairRations(n,b))
