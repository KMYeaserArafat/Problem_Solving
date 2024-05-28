# Rock Climbing
"""
Question LinK : https://www.hackerrank.com/contests/target-samsung-13-nov19/challenges/rock-climbing
"""


n,m = map(int,input().split())
count = 0
for x in range(n):
    data = list(map(int,input().split()))[:m]
    for i in range(len(data)):
        if(data[i]==3):
            count+=1 
        elif data[i:i+3]==[1,1,1]:
            count+1
        else:
            count+=0

    
print(count)