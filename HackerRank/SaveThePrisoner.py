
n = int(input())

for x in range(n):
    arr = list(map(int,input().split()))
    result = (arr[1]+arr[2]-2)%arr[0]+1
    print(result)