# Adjency List,
'''
output : 
1  ->  2  edge weight:  1
1  ->  3  edge weight:  1
2  ->  3  edge weight:  3
3  ->  4  edge weight:  4
4  ->  1  edge weight:  5
Internal representation:  {1: [[2, 1], [3, 1]], 2: [[3, 3]], 3: [[4, 4]], 4: [[1, 5]]}

'''


def AddVertex(vertex):
    global graph
    global verticesNo

    if vertex in graph:
        print("Vertex ", vertex, " already exists.")
    else:
        verticesNo = verticesNo+1
        graph[vertex] = []



def AddEdge(vertex1,vertex2,edge):
    global graph

    if vertex1 not in graph:
        print("Vertex ",vertex1," doesn't exist")
    elif vertex2 not in graph:
        print("Vertex ",vertex2," doesn't exist")
    else:
        temp = [vertex2,edge]
        graph[vertex1].append(temp)


def PrintGraph():
    global graph
    for vertex in graph:
        for edges in graph[vertex]:
            print(vertex, "-> ", edges[0], " edge weight ", edges[1])


graph = {}
verticesNo = 0

AddVertex(1)
AddVertex(2)
AddVertex(3)
AddVertex(4)

AddEdge(1,2,1)
AddEdge(1,3,1)
AddEdge(2,3,3)
AddEdge(3,4,4)
AddEdge(4,1,5)

PrintGraph()
print("Internal representation ", graph)

