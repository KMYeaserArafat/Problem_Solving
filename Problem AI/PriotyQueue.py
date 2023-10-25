#Prioty Queue ->Speacial Type Of Queue
'''
here mainly findout the solution by condition, 
here we delete the max number, 
'''

class PriotyQueue:
    def __init__(self) -> None:
        self.priotyQueue = []


    def Insert(self,data):
        self.priotyQueue.append(data)


    def Delete(self):
        maxData = max(self.priotyQueue)

        for x in range(len(self.priotyQueue)):
            if self.priotyQueue[x]==maxData:
                print("Max Index No : ", x)
                return self.priotyQueue.pop(x)




    def display(self):
        print(self.priotyQueue)



pq = PriotyQueue()
pq.Insert(10)
pq.Insert(20)
pq.Insert(90)
pq.Insert(40)
pq.Insert(50)
pq.Insert(70)

pq.display()

pq.Delete()
pq.display()

