'''
4.	The Newton-Raphson method is a way to quickly find a good approximation for the root of a real-valued function f(x) = 0. 
'''


# equation of function, f(x) = x**2-4x-7 = 0, 
#here initial point : x = 5


def func(x):
    y = x**2-4*x-7
    return y

def derivation(x):
    y = 2*x-4*x-7
    return y



def NewtonRapSon(x):
    h = func(x)/derivation(x)

    if abs(h)>=0.001:
        h = func(x)/derivation(x)
        x= x-h

    return x


rootValue = NewtonRapSon(5)

print("The root eqation : ",rootValue)


#Showing in graph,
import matplotlib.pyplot as plt


plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
x = [4]
y = [3]
plt.xlim(0, rootValue)
plt.ylim(0, rootValue)
plt.grid()
plt.plot(x, y, marker="o", markersize=10, markeredgecolor="red", markerfacecolor="green")
plt.show()