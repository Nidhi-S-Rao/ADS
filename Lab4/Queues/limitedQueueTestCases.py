from limitedQueue import *
def testEmptyQueue():
    s1=limitedQueue()
    assert(s1.getCount()==0)
    assert(s1.isQueueEmpty()==True)
    assert(s1.isQueueFull()==False)

def testEnqueue():
    s2=limitedQueue()
    s2.enqueue(10)
    assert(s2.getCount()==1)
    assert(s2.peek()==10)

def testDequeue():
    s3=limitedQueue()
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

testEmptyQueue()
testEnqueue()
testDequeue()
    


    