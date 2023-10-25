'''
Finding the root of equation : x^3-2x+1

'''
from pylab import *

def funx(x):
    y = x**3-2*x+1
    return y

x = linspace(-3,3,10)


def derivation(x):
    h = 0.000001
    derivate = funx(x+h)-funx(x)/h
    return derivate

def NewtonRapson(x):
    rapson = x-(funx(x)/derivation(x))
    return rapson

def iterative(a,b):
    x = a

    for i in range(b):
        x = NewtonRapson(x)

    return x

print("The Root of equation : ", iterative(1,3))

#Show In the Graph : 
plot(x,funx(x))
grid(True)
show()


