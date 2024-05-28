"""
Fraudulent Activity Notifications
"""

import statistics

def activityNotifications(expenditure,d):
    size = len(expenditure)
    count = 0
    DataStore = []
    for i in range(size-d+1):
        data = expenditure[i:i+d]
        DataStore.append(data)

    
    for x in range(len(DataStore)):
        meanValue = statistics.mean(DataStore[x])
        if(meanValue*2>=expenditure[data+1]):
            count+=1
        else:
            count+=1


    return count

n,d = map(int,input().rsplit())
expenditure = list(map(int,input().split()))[:n]
print(activityNotifications(expenditure,d))


