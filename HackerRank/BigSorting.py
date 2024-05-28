
def bigSorting(unsorted):
    sorting = sorted(unsorted)

    for x in range(len(sorting)):
        print(sorting[x])

n = int(input())
unsorted = []
for i in range(n):
    inputValue = int(input())
    unsorted.append(inputValue)

bigSorting(unsorted)