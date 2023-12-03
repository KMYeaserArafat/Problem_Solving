import math


node = []
edge = []

def AddNode(nodeValue):
    node.append(nodeValue)

def AddEdge(edgeValue):
    edge.append(edgeValue)


def funMethod(data):
    g = 1/(1+math.exp(-data))
    return g


#Add Node,
AddNode(float(input("i1 : ")))
AddNode(float(input("i1 : ")))

#AddEdge,
AddEdge(float(input("w1 : ")))
AddEdge(float(input("w2 : ")))
AddEdge(float(input("w3 : ")))
AddEdge(float(input("w4 : ")))

h1 = (node[0]*edge[0]) + (node[0]*edge[1])
h2 = (node[1]*edge[1]) + (node[1]*edge[3])

funh1 = funMethod(h1)
funh2 = funMethod(h2)
finalNode = funh1+funh2
AddNode(finalNode)
AddEdge(funh1)
AddEdge(funh2)

print("i1, i2, i3 : ", node)
print("w1, w2, w3, w4, w5, w6 : ", edge)
