'''
#User Input Programe, 
find out the middle points, 
all point multiplies by 2
show these data graphitically,
'''

import matplotlib.pyplot as mplt



#Find out the middle points, 
def FindPoints(lower,upper,n):
    xPoints = []

    del_h = (upper-lower)/n
    xPoints.append(lower)
    for x in range(0,n):
        xPoints.append(xPoints[x]+del_h)

    return xPoints


#Multiplies by 2 method, 
def multipliFun(Xpoints):
    yPoints = []
    for x in range(0,len(Xpoints)):
        yPoints.append(Xpoints[x]**2)

    return yPoints



lower = int(input("Enter Low point   : "))
upper = int(input("Enter Upper Point : "))
n = int(input("How many points want-to find out : "))

if(lower==upper or lower>upper):
    print("Invalid")
else:
    Xpoints = FindPoints(lower,upper,n)
    print(f"{lower} to {upper}, {n} middle points are : ", Xpoints)
    Ypoints = multipliFun(Xpoints)
    print("New Y Points : ", Ypoints)
    
    # Show Graphitically,
    mplt.plot(Xpoints,Ypoints)
    mplt.show()