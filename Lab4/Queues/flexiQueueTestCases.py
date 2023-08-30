from flexiQueue import *
def testEmptyQueue():
    s1=FlexiQueue()
    assert(s1.length()==0)
    assert(s1.isEmpty()==True)

def testEnqueue():
    s2=FlexiQueue()
    s2.enqueue(10)
    assert(s2.length()==1)

def testDequeue():
    s3=FlexiQueue()
    assert(s3.getSize()==2)
    s3.enqueue(20)
    s3.enqueue(30)
    assert(s3.getSize()==2)
    s3.enqueue(40)
    assert(s3.getSize()==4)
    assert(s3.dequeue()==20)
    assert(s3.length()==2)
    assert(s3.dequeue()==30)
    assert(s3.getSize()==2)
testEmptyQueue()
testEnqueue()
testDequeue()
    


    