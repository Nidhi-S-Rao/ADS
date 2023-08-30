class limitedQueue:
    def __init__(self):
        self.count=0
        #Setting the size of the queue
        self.data=[None]*5
        self.front=-1
    def isQueueFull(self):
        return self.count>=len(self.data)#Checking if queue is full
    def isQueueEmpty(self):
        return self.count==0 
    def getCount(self):
        return self.count#Getting the number of elements in queue
    def enqueue(self,element):
        if not self.isQueueFull():#Checking if queue is full
            self.front+=1#if queue is not full then increment the front and enqueue the lement in the index of front
            self.data[self.front]=element
            self.count+=1
            return self.count
        else:
            return None
    def dequeue(self):
        if not self.isQueueEmpty():
            self.count-=1
            return self.data.pop(0)
        else:
            return None
    def peek(self):
        if not self.isQueueEmpty():
            return self.data[0]
        else:
            return None
    def printElements(self):
        return self.data



    