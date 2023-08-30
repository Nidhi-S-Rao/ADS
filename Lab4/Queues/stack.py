class stack:
    def __init__(self):
        self.count=0
        self.data=[]
    def isStackEmpty(self):
        return self.count==0
    def getCount(self):
        return self.count
    def push(self,element):
        self.data.append(element)
        self.count+=1
        return self.count
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



    