
#Taum and B'day

t = int(input())

for x in range(t):
    b,w = map(int,input().split())
    bc,wc,z = map(int,input().split())

    if(bc+z<wc):
        print(b*x+w*(x+z))
    elif(wc+z<bc):
        print(w*wc+b*(wc+z))
    else:
        print(b*bc+w*wc)
