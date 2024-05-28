
# Super-Reduced-String, 

def SuperReducedString(stringData):
    Datalist = list(stringData)
    result = []

    for x in range(len(Datalist)):
        countData = Datalist.count(Datalist[x])
        if(countData%2 !=0 and Datalist[x] not in result):
            result.append(Datalist[x])

    if(len(result)==0):
        return "Empty"
    else:
        strData = ''.join(result)
        return strData

stringData = input().lower()
print(SuperReducedString(stringData))
