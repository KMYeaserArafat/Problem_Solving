# Ranker-Rank-In-a-String, 

word = "hackerrank"
t = int(input())

for x in range(t):
    s = str(input())
    p = 0
    wi = 0

    for wi in range(len(word)):
        if wi<9:
            p = s.find(word[wi],p)+1
            if p == 0:
                break
    
    if wi==9:
        print("Yes")
    else:
        print("NO")