#Adjency-Matrix
"""
1  ->  2  edge weight:  1
1  ->  3  edge weight:  1
2  ->  3  edge weight:  3
3  ->  4  edge weight:  4
4  ->  1  edge weight:  5
Internal representation:  [[0, 1, 1, 0], [0, 0, 3, 0], [0, 0, 0, 4], [5, 0, 0, 0]]

"""

def AddVertex(vertex):
    global graph
    global vertexsNo
    global vertexes

    if vertex in vertexes:
        print("Vartex ",vertex, " already exists")
    else:
        vertexsNo = vertexsNo+1
        vertexes.append(vertex)
        if vertexsNo>1:
            for v in graph:
                v.append(0)
        temp = []
        for i in range(vertexsNo):
            temp.append(0)
        graph.append(temp)



def AddEdge(vertex1,vertex2,edge):
    global graph
    global vertexes
    global vertexsNo

    if vertex1 not in vertexes:
        print("Vertex", vertex1," doesn't exists")
    elif vertex2 not in vertexes:
        print("Vertex",vertex2," doesn;t exists" )
    else:
        index1 = vertexes.index(vertex1)
        index2 = vertexes.index(vertex2)
        graph[index1][index2] = edge

def PrintGraph():
    global vertexes
    global graph
    global vertexsNo

    for i in range(vertexsNo):
        for j in range(vertexsNo):
            if graph[i][j] != 0:
                print(vertexes[i],"-> ", vertexes[j], "Edge Weight : ", graph[i][j])


graph = []
vertexsNo = 0
vertexes = []

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

print("Internal representaion : ", graph)