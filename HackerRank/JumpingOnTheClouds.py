

def jumpingOnTheClouds(c):
    res = 0
    ind = 0
    
    while ind != len(c)-1:
        if ind != len(c)-2 and c[ind+2] == 0:
            ind += 2
        else:
            ind += 1
        res += 1
        
    return res
                  
                


n = int(input())
arr = list(map(int,input().split()))
print(jumpingOnTheClouds(arr))
