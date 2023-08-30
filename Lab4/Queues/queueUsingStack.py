from stack import *


class queueUsingStack:
    def __init__(self):
        #Initializing 2 stacks
        self.s1=stack()
        self.s2=stack()
    def enqueueNew(self,ele):
        #Enquing to queue is same as pushing the elemnt to stack
        #using the push function used in stack
        self.s1.push(ele)
        return self.s1.count
    def dequeueNew(self):
        #To dequeue an element we need to get the rear element but in stack we can have only top element
        #pop elemnt from stack until we find the last element and push it to new stack S2. the last element from S1 popped will be the front
        #element. Then again from S2 pop element to s1.
        while(self.s1.getCount()>1):
            self.s2.push(self.s1.pop())
        ele=self.s1.pop()
        while(self.s2.getCount()>0):
            self.s1.push(self.s2.pop())
        return ele
    def peekNew(self):
        while(self.s1.getCount()>1):
            self.s2.push(self.s1.pop())
        ele=self.s1.peek()
        self.s2.push(self.s1.pop())
        while(self.s2.getCount()>0):
            self.s1.push(self.s2.pop())
        return ele
    

q1=queueUsingStack()
assert(q1.enqueueNew(10)==1)
assert(q1.enqueueNew(20)==2)
assert(q1.enqueueNew(30)==3)
assert(q1.dequeueNew()==10)
assert(q1.peekNew()==20)