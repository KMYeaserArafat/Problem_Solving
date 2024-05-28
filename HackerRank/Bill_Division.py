
n,k = map(int,input().split())
bill = list(map(int,input().split()))

l = int(input())

b = sum(bill)-bill[k]/2

if(b==l):
    print("Bon Appetit")

else:
    print(b-l)


