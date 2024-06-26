# Palindrome Index, 

#abab

def palindromeIndex(s):
    if(s==s[::-1]):
        return -1
    
    n = len(s)
    
    for i in range(n//2):
        if(s[i]!=s[n-1-i][::-1]):
            if(s[i:n-1-i] == s[i:n-1-i][::-1]):
                return n-1-i
            elif(s[i+1:n-i]== s[i+1:n-i][::-1]):
                return i    
    return -1
           

for n in range(int(input())):
    s = input()
    print(palindromeIndex(s))