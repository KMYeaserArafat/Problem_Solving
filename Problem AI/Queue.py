# Queue :-> FIFO
'''
for the queue, 
===================

1. enQueue,
2. Dequeue,
3. showQueue
4. sizeOfQueue

'''


class Queue:

    def __init__(self) -> None:
        self.queue = []

    
    def enQueue(self,iteam):
        self.queue.append(iteam)

    def DeQueue(self):
        if len(self.queue)<1:
            return 0
        return self.queue.pop(0)
    

    def showQueue(self):
        print(self.queue)

    def sizeOfQueue(self):
        print("Size Of Queue : ",len(self.queue))


q1 = Queue()
q1.enQueue(10)
q1.enQueue(20)
q1.enQueue(30)
q1.enQueue(40)
q1.enQueue(50)

q1.showQueue()
q1.sizeOfQueue()

q1.DeQueue()
q1.showQueue()



