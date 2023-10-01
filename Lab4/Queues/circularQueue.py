class circularQueue:
    def __init__(self):
        self.count=0
        #Setting the size of the queue
        self.data=[None]*5
        self.front=-1
        self.rear=-1
    def isQueueFull(self):
        return self.count>=len(self.data)#Checking if queue is full
    def isQueueEmpty(self):
        return self.count==0 
    def getCount(self):
        return self.count#Getting the number of elements in queue
    def enqueue(self,element):
        if not self.isQueueFull():#Checking if queue is full
            self.front=(self.front+1)%len(self.data)#if queue is not full then increment the front and enqueue the lement in the index of front
            self.data[self.front]=element
            self.count+=1
            return self.count
        else:
            return None
    def dequeue(self):
        if not self.isQueueEmpty():
            self.count-=1
            self.rear=(self.rear+1)%len(self.data)
            item=self.data[self.rear]
            self.resize(self.data,self.rear,self.front)
            return item
        else:
            return None
    def peek(self):
        if not self.isQueueEmpty():
            return self.data[0]
        else:
            return None
    def printElements(self):
        l=[]
        for i in (self.data):
            if not i==None:
                l.append(i)
        return l
    
    def resize(self,q,r,f):
        oldData=q
        for i in range(r+1):
            q[i]=None
        for i in range(r+1,f+1):
            q[i]=oldData[i]
        




s3=circularQueue()
s3.enqueue(20)
s3.enqueue(30)
s3.enqueue(40)
s3.enqueue(50)
s3.enqueue(60)
assert(s3.isQueueFull()==True)
assert(s3.getCount()==5)
assert(s3.peek()==20)
assert(s3.dequeue()==20)
assert(s3.getCount()==4)
assert(s3.printElements()==([30,40,50,60]))
assert(s3.getCount()==4)
s3.enqueue(10)
assert(s3.printElements()==([10,30,40,50,60]))