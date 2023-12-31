#Jumping On the Clouds, 


def jumpingOnClouds(n,k,c):
    e = 100
    jump = (0+k)%n
    if c[jump]==1:
        e-=3
    else:
        e-=1
    while jump !=0:
        jump = (jump+k)%n
        if c[jump]==1:
            e-=3
        else:
            e-=1
    return e
    

n,k = map(int,input().split())
c = list(map(int,input().split()))
print(jumpingOnClouds(n,k,c))


