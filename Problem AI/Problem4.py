'''
#Find out the points into lower,upper points.
show points by grapitical
'''

import matplotlib.pyplot as plt



def FindPoints(low,upper,n):
    points = []

    del_h = (upper-low)/n
    points.append(low)
    for x in range(0,n):
        points.append(points[x]+del_h)

    return points


low = int(input("Enter a lower number : "))
upper = int(input("Enter a Upper Number : "))
n = int(input("How many point want-to find out : "))

if(low==upper or low>upper):
    print("It's not work !!")
else:
    print("New Points : ", FindPoints(low,upper,n))
    #show point by graphitical,
    plt.plot(FindPoints(low,upper,n))
    plt.show()