# Absolute Permulation

def AbsolutePermulation(n,k):
    pos = []
    result = []
    for a in range(1,n+1):
        pos.append(a)

    for i in range(len(pos)):
        for j in range(len(pos)):
            if abs(pos[i]-pos[j])==k:
               result.append(pos[j])

    
    if len(pos)==len(result):
        return result
    else:
        return -1
   

t = int(input())
for a in range(t):
    n,k =  map(int,input().split())
    print(AbsolutePermulation(n,k))
