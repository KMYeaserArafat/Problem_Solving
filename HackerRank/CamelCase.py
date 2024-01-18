
# Camel Case, 

def camelCase(s):
    slist = list(s)
    count = 0

    for x in range(1,len(slist)):
        if(slist[0] == slist[x].lower()):
            count+=1
        elif(slist[x] == slist[x].upper()):
            count+=1
        
    print(count)
   

s = str(input())
camelCase(s)
