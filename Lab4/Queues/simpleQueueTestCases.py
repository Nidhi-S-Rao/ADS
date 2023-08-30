from simpleQueue import *
def testEmptyQueue():
    s1=SimpleQueue()
    assert(s1.getElementCount()==0)
    assert(s1.isQueueEmpty()==True)

def testEnqueue():
    s2=SimpleQueue()
    s2.enqueue(10)
    assert(s2.getElementCount()==1)
    assert(s2.peek()==10)

def testDequeue():
    s3=SimpleQueue()
    s3.enqueue(20)
    s3.enqueue(30)
    s3.enqueue(40)
    assert(s3.getElementCount()==3)
    assert(s3.peek()==20)
    assert(s3.dequeue()==20)
    assert(s3.getElementCount()==2)
    assert(s3.printElements()==([30,40]))

testEmptyQueue()
testEnqueue()
testDequeue()
    


    