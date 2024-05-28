'''
write a programe using python, 
n = 4
arr = [5,2,8,3]

output willbe: 
5 5 5 5 5 
2 2 
8 8 8 8 8 8 8 8
3 3 3

sumation arr = [25,4,64,9]
'''
n  = int(input())
arr1 = list(map(int,input().split()))[:n]
arr2 = []
arr3 = []
sumArr = []

for num in arr1:
    Data = (str(num)+' ')*num
    print(Data)
    arr2.append(Data)


for x in arr2:
    Data = x.split(' ')
    arr3.append(Data)


arr4 = []
for i in range(0,len(arr3)):
    int_List = [int(x) for x in arr3[i] if x.isdigit()]
    arr4.append(int_List)

for j in range(0,len(arr4)):
    DataSum = sum(arr4[j])
    sumArr.append(DataSum)
    
print("Sumation Array : ",sumArr)




    

