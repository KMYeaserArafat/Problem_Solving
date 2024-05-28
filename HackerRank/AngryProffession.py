#Angry Proffessor, 


t = int(input())

for x in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))

    studentCount = 0

    for x in range(len(a)):
        if(a[x]<=0):
            studentCount+=1

    
    if(studentCount>=k):
        print("NO")
    else:
        print("YES")