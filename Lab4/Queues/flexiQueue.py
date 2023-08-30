class FlexiQueue:
    defaultSize=2
    def __init__(self):
        #setting the default size of the queue
        self.data=[None]*FlexiQueue.defaultSize
        self.front=0
        self.count=0
    #Method to get the number of elements in the queue
    def length(self):
        return self.count
    #Method to check if the queue is empty
    def isEmpty(self):
        return self.count==0
    #Method to get the first element in queue
    def getFirst(self):
        if not self.isEmpty():
            return self.data[self.front]
        else:
            return None
    def enqueue(self, ele):
        #Condition to check if the queue is full, if its full resizing the queue
        if self.count==len(self.data):
            self.resize(2*len(self.data))
        idx=(self.front+self.count)%len(self.data)
        self.data[idx]=ele
        self.count+=1
        return self.count
    def dequeue(self):
        if not self.isEmpty():
            ele=self.data[self.front]
            self.count-=1
            self.data[self.front]=None
            #Again shrinking the queue size once deleting the element
            self.front=(self.front+1)%len(self.data)
            if 0<len(self.data)//4:
                self.resize(len(self.data)//2)
            return ele
        else:
            return None
    def resize(self,cap):
        oldData=self.data
        walk=self.front
        self.data=[None]*cap
        for k in range(self.count):
            self.data[k]=oldData[walk]
            walk=(walk+1)%len(oldData)
        self.front=0

    def getSize(self):
        return len(self.data)
