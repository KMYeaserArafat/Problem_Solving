'''
finding the root of equation : x^3-x^2+2

'''


def functionx(x):
    y = (x**3-x**2)+2
    return y

def derivation(x):
    y = (3*x**2)-(2*x)
    return y

def NewtonRapson(x):
    h = functionx(x)/derivation(x)

    if abs(h)>=0.001:
        h = functionx(x)/derivation(x)
        x = x-h
    
    return x


print("The Root of equation is : ", NewtonRapson(2))