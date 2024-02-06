
# Funny- String, 

def funnyString(s):
    #Acending-Order, 
    valueListOfAsending = list(bytes(s, 'ascii'))
    AsendingDataList = []
    for x in range(1,len(valueListOfAsending)):
        if(valueListOfAsending[x]>valueListOfAsending[x-1]):
            value=valueListOfAsending[x]-valueListOfAsending[x-1]
            AsendingDataList.append(value)
        else:
            value=valueListOfAsending[x-1]-valueListOfAsending[x]
            AsendingDataList.append(value)

    #Desenting-Order,
    valueListOfAsending.sort(reverse=True)
    DesendingDataList = []
    for x in range(1,len(valueListOfAsending)):
        if(valueListOfAsending[x]>valueListOfAsending[x-1]):
            value = valueListOfAsending[x]-valueListOfAsending[x-1]
            DesendingDataList.append(value)
        else:
            value = valueListOfAsending[x-1]-valueListOfAsending[x]
            DesendingDataList.append(value)

    
    #Main-Condition, 
    for x in AsendingDataList:
        for y in DesendingDataList:
            if(x==y):
                return "Funny"
            else:
                return "Not Funny"

q = int(input())
for t in range(q):
    s = input()
    print(funnyString(s))