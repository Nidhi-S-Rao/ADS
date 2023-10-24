
class maxHeap:
    def __init__(self,lst=[]):
        self.data=lst
        self._buildHeap_()
    def isEmpty(self):
        return len(self.data)==0
    #Getting the count of heap
    def getCount(self):
        return len(self.data)
    def _parent_(self,idx):
        return (idx-1)//2
    def _lchild(Self,idx):
        return (2*idx+1)
    def _rchild(self,idx):
        return (2*idx+2)
    def _swap_(self,i,j):
        self.data[i],self.data[j]=self.data[j],self.data[i]
    def _buildHeap_(self):
        length=len(self.data)
        start=(length-2)//2
        for idx in range(start,-1,-1):
            self._downHeap_(idx,length)
    def _downHeap_(self,idx,length):
        if(self._lchild(idx)<length):
            left=self._lchild(idx)
            bigChild=left
            if(self._rchild(idx)<length):
                right=self._rchild(idx)
                if(self.data[right]>self.data[left]):
                    bigChild=right
            if self.data[bigChild]>self.data[idx]:
                self._swap_(bigChild,idx)
                self._downHeap_(bigChild,length)
    #Adding a new element
    def addElement(self,key):
        self.data.append(key)
        self._upHeap_(len(self.data)-1)
    
    def _upHeap_(self,j):
        parent=self._parent_(j)
        if(j>0 and self.data[j]>self.data[parent]):
            self._swap_(j,parent)
            self._upHeap_(parent)
    #Getting the maximum element
    def getMaxElement(self):
        return(self.data[0])
    #Deleting the max element
    def delete(self):
        self._swap_(0,len(self.data)-1)
        ele=self.data.pop()
        self._downHeap_(0,len(self.data)-1)
        return ele
    
    #Method to test the heap order property
    def testMAxHeap(self):
        if not self.isEmpty():
            for idx in range(len(self.data)-1,0,-1):
                assert(self.data[idx]<=self.data[self._parent_(idx)])

    #Method for heap sorting
    def heapSort(self):
        if not self.isEmpty():
            for i in range(len(self.data)-1,0,-1):
                self._swap_(0,i)
                self._downHeap_(0,i)
            return self.data


heap=maxHeap()
heap.addElement(50)
heap.addElement(10)
heap.addElement(15)
heap.addElement(60)
heap.addElement(90)
heap.addElement(5)
heap.addElement(75)
heap.testMAxHeap()
assert(heap.getCount()==7)
assert(heap.getMaxElement()==90)
assert(heap.delete()==90)
assert(heap.getMaxElement()==75)
assert(heap.delete()==75)
assert(heap.getMaxElement()==60)
assert(heap.heapSort()==([5, 10, 15, 50, 60]))