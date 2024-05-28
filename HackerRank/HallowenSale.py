#Hallowen Sale, 

p,d,m,s = map(int,input().split())

cost = p
l = []

while(sum(l)<=s):
    if cost>m:
        l.append(cost)
        cost = cost-d
    if cost<=m:
        l.append(m)
print(len(l)-1)