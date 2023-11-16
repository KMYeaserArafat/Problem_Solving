#BFS -> 
"""
       A
      / \
     B   C
    / \   \
   D  E--->F

"""

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F':[]
}

visited = []
queue = []

def BFS(graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s, end=" ")

        for x in graph[s]:
            if x not in visited:
                visited.append(x)
                queue.append(x)


BFS(graph,'A')
                
    