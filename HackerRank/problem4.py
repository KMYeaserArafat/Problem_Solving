'''
atfirst declear a[] & b[] 2 array, 

If a[i] > b[i], then Alice is awarded 1 point.
If a[i] < b[i], then Bob is awarded 1 point.
If a[i] = b[i], then neither person receives a point.

Input 
17 28 30
99 16 8

Output
2 1

'''

def compareTripletes(a,b):
    Alice = 0
    Bob = 0

    for i in range(len(a)):
        if a[i]>b[i]:
            Alice +=1
        elif a[i]<b[i]:
            Bob+=1
        elif a[i]==b[i]:
            #print("neither person recieves a point")
            pass
    
    # print(f"Alice is awarded {Alice} point")
    # print(f"Bob is awrded {Bob} point")
    print(f"{Alice} {Bob}")




a = []
b = []

inputValue_A = input()
sData_A  = inputValue_A.split(" ")
a = [int(num1) for num1 in sData_A]  # To convert split str data type to int data type, 

inputValue_B = input()
sData_B = inputValue_B.split(" ")
b = [int(num2) for num2 in sData_B] 

compareTripletes(a,b)


        






