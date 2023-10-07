"""
Sumation of list Data, 

"""
def DataSum(DataStore):
    s = 0
    for x in range(0,len(DataStore)):
        s = s + DataStore[x]

    return s


DataStore = [10,20,30,40,50]
print("Show All Data : ")
print("Sumation of DataStore : ", DataSum(DataStore))