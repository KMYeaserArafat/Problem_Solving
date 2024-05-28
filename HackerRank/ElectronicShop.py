
def getMoneySpent(keyboard,drives,b):
    total = -1
    
    for x in keyboard:
      for y in drives:
        z = x+y
        if(z>total and z<=b):
          total = z
    
    return total



b,n,m = map(int,input().split())

keyboard = list(map(int,input().split()))
drives = list(map(int,input().split()))

print(getMoneySpent(keyboard,drives,b))