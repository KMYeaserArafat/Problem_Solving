"""
Insert Data into a list, 

Sumation, 
Without1 Sumation : 14
Without2 Sumation : 13
Without3 Sumation : 12
Without4 Sumation : 11
Without5 Sumation : 10

find out the max and min number in here, 
"""

arr = []
arr2 = []

for x in range(5):
    inputData = input()
    arr.append(int(inputData))

print(arr)

for x in range(5):
    sum = 0
    for y in range(5):
        if(x!=y):
            sum += arr[y]


    arr2.append(sum)
    print(f"Without {x}, Sumation : ", sum)

minData = min(arr2)
maxData = max(arr2)

print(minData,maxData)
