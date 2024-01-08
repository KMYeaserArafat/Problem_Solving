#Flat-Land Space, 

def flatLandSpace(n,m,c):
    result = []
    result0 = []
    result1 = []
    minvalue = min(c)
    maxvalue = max(c)

    for x in range(minvalue,maxvalue+1):
        result.append(x)


    for a in range(len(c)):
        for x in range(len(result)):
            Data = abs(result[x]-c[a])
            result0.append(Data)
            
    finalresult = []
        
    for b in range(len(result0)):
        if result0[b]<=m:
            finalresult.append(result0[b])

    maxData = max(finalresult)

    return maxData

n,m = map(int,input().split())
c = list(map(int,input().split()))
if n==m:
    print(0)
else:
    print(flatLandSpace(n,m,c))
