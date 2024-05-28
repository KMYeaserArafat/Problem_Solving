

def method1(d,arr):
    i=0
    j=1
    z=2

    Data1 = arr[j]-arr[i]
    Data2 = arr[z]-arr[j]

    if(Data1==Data2 and Data1==d):
        print(d)
    else:
        print("Wrong")

n,d = map(int,input().split())
arr = list(map(int,input().split()))

a = []
b = []
c = []

for x in range(0,n,d-1):
    a.append(arr[x])

for y in range(1,n,d-1):
    b.append(arr[y])

for z in range(2,n,d-1):
    c.append(arr[z])

print(a)
print(b)
print(c)

method1(d,a)
method1(d,b)
method1(d,c)


    

