'''
finding the root of equation : 3x-cosx-1

'''
from pylab import *


def functionx(x):
    y = 3*x-np.cos(x)-1
    return y

x = linspace(-3,3,10)

def Derivative(x):
    h = 0.000001
    derivative = functionx(x+h)-functionx(x)/h
    return derivative

def NewtonRapson(x):
    rapson = x-(functionx(x)/Derivative(x))
    return rapson

def Iterative(a,b):
    x = a
    for i in range(b):
        x = NewtonRapson(x)
    
    return x

print("The Root of equation : ", Iterative(1,3))


#Show In the curve, 
plot(x,functionx(x))
grid(True)
show()

