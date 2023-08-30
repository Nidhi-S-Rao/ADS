from simpleQueue import *

class findMaxElement:
    def __init__(self):
        #Initializing 2 queues
        self.q1=SimpleQueue()
        self.q2=SimpleQueue()
    #Method to print the elements in the queue from rear to front
    def printElements(self):
        return self.q1.printElements()
    #Method to find the maximum element
    def findMax(self):
        self.max=0
        #We will dequeue every element from queue compare it with a variable maximum and if it more than max, max will be updated with the new value
        #and that element will be enqueued to new queue and again all elements from new queue will dequeued and added to original queue
        while(self.q1.getElementCount()>0):
            ele=self.q1.dequeue()
            if(self.max<ele):
                self.max=ele
            self.q2.enqueue(ele)
        while(self.q2.getElementCount()>0):
            self.q1.enqueue(self.q2.dequeue())
        return self.max
    

s1=findMaxElement()
assert(s1.q1.enqueue(40)==1)
assert(s1.q1.enqueue(10)==2)
assert(s1.q1.enqueue(30)==3)
assert(s1.findMax()==40)
assert(s1.q1.dequeue()==40)
assert(s1.findMax()==30)