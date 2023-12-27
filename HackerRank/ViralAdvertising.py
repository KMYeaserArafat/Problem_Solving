import math

n = int(input())

people=5
result = 0

for x in range(1,n+1):
    half = math.floor(people/2)
    result += half
    people = 3*half

print(result)