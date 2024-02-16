
# Alternating Characters
def alternatingCharacters(arr):
    data = list(arr)
    count = 0
    for x in range(1,len(data)):
        if(data[x]==data[x-1]):
            count+=1

    return count


n = int(input())
for x in range(n):
    arr = input()
    print(alternatingCharacters(arr))