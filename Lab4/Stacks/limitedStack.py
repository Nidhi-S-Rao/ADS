class stack:
    def __init__(self):
        self.count=0
        self.data=[None]*5
        self.top=-1
    def isStackFull(self):
        #Method to check if stack is full. If the count is more than the default size then stack is full
        return self.count>=len(self.data)
    def isStackEmpty(self):
        return self.count==0
    def getCount(self):
        return self.count
    def push(self,element):
        if not self.isStackFull():
            #If stack is not full then top is incremented and the element is pushed
            self.top+=1
            self.data[self.top]=element
            self.count+=1
            return self.count
        else:
            return None
    def pop(self):
        if not self.isStackEmpty():
            #Popping the last element from the stack
            self.count-=1
            return self.data.pop(self.top)
        else:
            return None
    def peek(self):
        if not self.isStackEmpty():
            return self.data[self.top]
        else:
            return None
    def printElements(self):
        return self.data



    