class stack:
    def __init__(self):
        self.count=0
        self.data=[]
        #Checking if stack is empty
    def isStackEmpty(self):
        return self.count==0
    #Getting the count of stack
    def getCount(self):
        return self.count
    #Adding the element to stack
    def push(self,element):
        self.data.append(element)
        self.count+=1
        return self.count
    #Removing the last element from stack
    def pop(self):
        if not self.isStackEmpty():
            self.count-=1
            return self.data.pop()
        else:
            return None
    def peek(self):
        if not self.isStackEmpty():
            return self.data[-1]
        else:
            return None
    def printElements(self):
        return self.data



    