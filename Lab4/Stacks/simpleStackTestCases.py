from stack import *
def testEmptyStack():
    s1=stack()
    assert(s1.getCount()==0)
    assert(s1.isStackEmpty()==True)

def testPush():
    s2=stack()
    s2.push(10)
    assert(s2.getCount()==1)
    assert(s2.peek()==10)

def testPop():
    s3=stack()
    s3.push(20)
    s3.push(30)
    s3.push(40)
    assert(s3.getCount()==3)
    assert(s3.peek()==40)
    assert(s3.pop()==40)
    assert(s3.getCount()==2)
    assert(s3.printElements()==([20,30]))

testEmptyStack()
testPush()
testPop()
    


    