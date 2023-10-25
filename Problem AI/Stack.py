# Stack -> LIFO
'''
Push: Add an element to the top of a stack
Pop: Remove an element from the top of a stack
IsEmpty: Check if the stack is empty
IsFull: Check if the stack is full
Peek: Get the value of the top element without removing it
'''

class Stack:
    
    def __init__(self) -> None:
        self.stack = []
        self.maxsize = 4

    def IsFull(self):
        if len(self.stack) == self.maxsize:
            print("Stack is full,Can't Insert Data")
            return 0
        elif len(self.stack)<4:
            print("Stack Have more space,you can insert Data, ")
            
        return 1


    def Push(self,iteam):
        if self.IsFull() != 0:
            print(f"Insert Data : {iteam}")
            self.stack.append(iteam)

    
    def IsEmpty(self):
        if len(self.stack) == 0:
            print("Stack is empty,can't possible to Pop")
            return 0
        else:
            print("Pop Data sucessed")

        return 1


    def Pop(self):
        if self.IsEmpty() !=0:
            self.stack.pop()

    
    def Display(self):
        print("Show Stack : ", self.stack)



s1 = Stack()
s1.Push(10)
s1.Push(20)
s1.Push(39)
s1.Push(10)
s1.Push(20)
s1.Push(39)
s1.Display()
s1.Pop()

s1.Display()