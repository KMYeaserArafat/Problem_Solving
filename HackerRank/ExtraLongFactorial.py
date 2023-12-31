#Extra-Long-Factirial

def factorial(n):
    answer = 1

    if(n==0):
        return 0
    while(n>0):
        answer*=n
        n-=1
    return answer

n = int(input())
print(factorial(n))