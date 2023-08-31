from simpleQueue import *
from stack import *


class Rotate:
    #Contents of queue can be rotated using a stack
    def __init__(self):
        self.q1=SimpleQueue()
        self.s1=stack()
    def rotateMethodUsingStack(self):
        while(self.q1.count>0):
            self.s1.push(self.q1.dequeue())
        while(self.s1.count>0):
            self.q1.enqueue(self.s1.pop())
        return self.q1.printElements()
    

q=Rotate()
q.q1.enqueue(10)
q.q1.enqueue(20)
q.q1.enqueue(30)
q.q1.enqueue(40)
assert(q.rotateMethodUsingStack()==([40,30,20,10]))




