#Cats & Mouse 

def catsAndMouse(q):
    for x in range(q):
      x,y,z = list(map(int,input().split()))
      d1 =  abs(x-z)
      d2 = abs(y-z)
      if(d1>d2):
        print("Cat B")
      elif(d1<d2):
        print("Cat A")
      else:
        print("Mouse C")
      
        

q = int(input())

catsAndMouse(q)