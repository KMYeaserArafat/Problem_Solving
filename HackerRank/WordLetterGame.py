# Word-Letter-Game, 
'''
The Game will Ask to write a word using a given letter, and while the word entered,
the programe will cheack the word if it has that character and show the result, 

Example : 
Input: 
How Many characters : 3
Must Have character : c
write your answer   : cat

Output: 
Your given word cat has 3 character and character c
'''

n = int(input("How Many Characters : "))
k = input("Must Have Character : ").lower()
w = input("Write your answer : ").lower()
wordlen = len(w)

if(n==wordlen and k in w):
    print(f"Your given word {w} has {n} character and character {k}")
else:
    print("Wrong")