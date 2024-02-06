# weighted Uniform String;

def weightedUniformString(s,queries):
    slist = list(s)
    sindexlist = []
    Datalist = []
    qCheackData = []

    for char in slist:
        if 'a'<=char<='z':
            indexData = ord(char)-ord('a')+1
            sindexlist.append(indexData)

    length = len(sindexlist)

    for x in range(0,length):
        if(sindexlist[x] != sindexlist[x-1]):
            Datalist.append(sindexlist[x-1])
        elif(sindexlist[x]==sindexlist[x-1]):
            sum = sindexlist[x]+sindexlist[x-1]
            Datalist.append(sum)
    
    # queries cheack, 
    for x in range(len(queries)):
        if(queries[x] in Datalist):
            qCheackData.append("YES")
        else:
            qCheackData.append("NO")

    return qCheackData



s = str(input())
n = int(input())
queries = []
for t in range(n):
    Data = int(input())
    queries.append(Data)

result = weightedUniformString(s,queries)
print(result)


    