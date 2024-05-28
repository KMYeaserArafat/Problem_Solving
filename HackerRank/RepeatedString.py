#Repeated-String, 

def repectedString(s,n):
    count = 0

    for x in s:
        if(x=="a"):
            count+=1
    print(count)
    

s = input()
n = int(input())
repectedString(s,n)

