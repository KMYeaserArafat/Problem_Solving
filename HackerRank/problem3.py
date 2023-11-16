'''
1. Declear an array size and input their values, 
2. create a plusMinus method where just pass 1 peramiter (arr), 
      In the method find out positive, negetive and zero 
3. find out the total positive, negetive and zero number and print their average !!
'''


def plusMinus(arr):
    positive = 0
    negative = 0
    zero = 0
    n = len(arr)

    for x in range(n):
        if arr[x]>0:
            positive+=1
        elif arr[x]<0:
            negative+=1
        elif arr[x]==0:
            zero+=1

    print(float(positive/n))
    print(float(negative/n))
    print(float(zero/n))



n = int(input("Enter Number : "))
arr = []

if n>0 and n<=100:
    for x in range(n):
        inputValue = int(input())
        if inputValue>=-100 and inputValue<=100:
            arr.append(inputValue)

print(arr)
plusMinus(arr)


