#Nuron Network,
'''
Student Name : K M Yeaser Arafat
Student ID : 21-44933-2

'''

import math 

class NutonNetwork:
    def __init__(self,) -> None:
        self.graph = []
        self.edge = []

    
    def InsertNodeValue(self,nodeValue):
        self.graph.append(nodeValue)

    def AddEdgeValue(self,edgeValue):
        self.edge.append(edgeValue)

    def Method1(self,data):
        g = 1/(1+math.exp(-data))
        return g
        

nn = NutonNetwork()
#here Take data for input node value, 
for x in range(2):
    nn.InsertNodeValue(float(input(f"Enter Input Node {x+1} Value : ")))

#here add edge value, 
for y in range(4):
    nn.AddEdgeValue(float(input(f"Edge value {y+1} : ")))

h1 = nn.graph[0] * nn.edge[0] + nn.graph[0]*nn.edge[1]
h2 = nn.graph[1] * nn.edge[2] + nn.graph[1]*nn.edge[3]

Datah1 = nn.Method1(h1)
Datah2 = nn.Method1(h2)

hData = Datah1+Datah2
ol = nn.Method1(hData)

nn.InsertNodeValue(ol)
nn.AddEdgeValue(Datah1)
nn.AddEdgeValue(Datah2)

for x in range(len(nn.graph)):
    print(f"i{x+1}: ", nn.graph[x], end=" ")

print()

for y in range(len(nn.edge)):
    print(f"w{y+1}: ", nn.edge[y], end=" ")












