#Beautiful-Days-At-the-Movies, 

def method1(arr,difference,k):
    a = 0
    for x in range(difference+1):
        a += abs(not (arr[x] - int(str(arr[x])[::-1]))%k)
    
    print(a)
        

s,e,k = map(int,input().split())

difference = e-s
arr = []

for x in range(difference+1):
    Data = s+x
    arr.append(Data)

method1(arr,difference,k)


