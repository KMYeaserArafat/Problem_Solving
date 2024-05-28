# Lottery, 
import random

n = int(input("How many number want-to input : "))
print("Enter the Token Number  : ",end="")
dataStore = list(map(int,input().split()))[:n]

toss = random.randint(0,n)

print(f"Show All Tocken Number : {dataStore}")
print(f"Toss Index : {toss}")
print(f"Select toss Token Number : {dataStore[toss]}")