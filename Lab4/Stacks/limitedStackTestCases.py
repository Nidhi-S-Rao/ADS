from limitedStack import *
def testEmptyStack():
    s1=stack()
    assert(s1.getCount()==0)
    assert(s1.isStackEmpty()==True)
    #print(s1.isStackFull())
    assert(s1.isStackFull()==False)

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
    s3.push(50)
    assert(s3.isStackFull()==False)
    s3.push(60)
    assert(s3.isStackFull()==True)
    assert(s3.getCount()==5)
    assert(s3.peek()==60)
    assert(s3.pop()==60)
    assert(s3.getCount()==4)
    assert(s3.printElements()==([20,30,40,50]))

testEmptyStack()
testPush()
testPop()
    


    