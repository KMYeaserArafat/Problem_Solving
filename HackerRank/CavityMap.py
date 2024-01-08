
#Cavity-Map,

def cavityMap(n,grid):
    result = []
    for x in range(n):
        Data = grid[x].replace('9','X')
        result.append(Data)

    for y in range(n):
        print(result[y])


n = int(input())
grid = list(input().split())
cavityMap(n,grid)


