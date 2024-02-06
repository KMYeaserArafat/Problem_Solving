# Pangrams

def Pangrams(s):
   #create a set with uniqe characters
    temp =  set(s.lower())-set(' ')

    #main logic : 
    if len(temp)==26:
        print("pangram")
    else:
        print("not pangram")



s = str(input())
Pangrams(s)