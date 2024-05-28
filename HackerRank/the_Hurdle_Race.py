#The Hurdle Race, 


n,k = map(int,input().split())
height = list(map(int,input().split()))

maxHeight = max(height)

if(k<maxHeight):
    ans = maxHeight-k
    print(ans)
else:
    print(0)
