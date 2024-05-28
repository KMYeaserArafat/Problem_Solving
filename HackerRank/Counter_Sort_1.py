
#Counter Sort-1

n = int(input())
arr = list(map(int,input().split()))[:n]

tot = [0]*100

for i in range(0,n):
    temp = arr[i]
    tot[temp]+=1

print(*tot, sep=' ')


