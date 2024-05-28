
# Intro The tutorial challenge, 

v = int(input())
n = int(input())
arr = list(map(int,input().rstrip().split()))[:n]

for x in range(len(arr)):
    if arr[x]==v:
        print(x)