#ACM TEAM ->Binary digit count, 

def acmTeam(people,n,m):
    maxSub = 0
    count = 0

    for i in range(n):
        for j in range(i,n):
            sub = 0
            for x,y in zip(people[i],people[j]):
                if(x=='1' or y=='1'):
                    sub+=1
            
            if sub>maxSub:
                maxSub = sub
                count = 1
            elif sub==maxSub:
                count+=1

    return [maxSub,count]


n,m = map(int,input().split())
people = [input() for i in range(n)]

