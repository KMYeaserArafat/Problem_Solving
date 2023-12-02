'''
/*
You are in charge of the cake for a child's birthday. 
You have decided the cake will have one candle for each year of their total age. 
They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

Input: 
---------
4
arr = [3, 2, 1,3]

Output:
----------
2
*/'''


n = int(input())
arr = []

for x in range(n):
    data = int(input())
    arr.append(data)

# Find the number with the maximum occurrences
max_occurrences_number = max(set(arr), key=arr.count)
# Find the maximum occurrences
max_occurrences_count = arr.count(max_occurrences_number)

print(max_occurrences_count)



