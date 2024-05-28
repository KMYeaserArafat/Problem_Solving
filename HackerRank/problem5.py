'''
A very big sum, 
----------------------
How many number want-to take . From User take this number and fillup their values, 


here use a method whose name is a veryBigSum, his datatype is long type. 

Input: 
5
10 20 40 50 60

Output: 
180


'''


n = int(input())
ValuesStore = list()

values = input()
s_values = values.split(" ")

for i in range(0,n):
   ValuesStore[i] = i

ValuesStore = [int(num) for num in s_values]
print(ValuesStore)
