


n = int(input())
arr = list(map(int,input().split()))

DataList = []

for i in range(n):
    for j in range(i+1, n):
        DataList.append(arr[i]+arr[j])
print(DataList)