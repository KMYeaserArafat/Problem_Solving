#factorial function, 
'''
5! = 5X4X3X2X1 = 120

'''
import math

def factorial(n):
    ans = 1
    if(n>=1):
        for x in range(1,n+1):
            ans*=x
    return ans



n = int(input())
print(factorial(n))


    

