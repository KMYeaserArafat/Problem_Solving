



class Scorecount:
    def __init__(self) -> None:
        self.score = []
        

    def InputData(self,Data):
        self.score.append(Data)
        



s = Scorecount()

n = int(input())
for x in range(n):
    id = int(input())
    s.InputData(id)

print(s.score)

maximum = s.score[0]
minimum = s.score[0]

max = 0
min = 0

for x in range(n):
    if(s.score[x]>maximum):
        maximum = s.score[x]
        max+=1
    
    if(s.score[x]<minimum):
        minimum = s.score[x]
        min+=1


print(max,min)

