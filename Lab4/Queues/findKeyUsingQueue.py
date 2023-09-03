from stack import *;
from simpleQueue import*;
#Program to check if key is present in the given stack using one stack and queue
def findKey(key):
    s1=stack()
    q1=SimpleQueue()
    s1.push(10)
    s1.push(20)
    s1.push(30)
    s1.push(40)
    f=0
    while(s1.count>0):
        ele=s1.pop()
        q1.enqueue(ele)
        if(key==ele):
            f=1
    copyQueueToStack(s1,q1)
    copyStackToQueue(s1,q1)
    copyQueueToStack(s1,q1)
    return f==1

def copyQueueToStack(s1,q1):
    while(q1.count>0):
        s1.push(q1.dequeue())

def copyStackToQueue(s1,q1):
    while(s1.count>0):
        q1.enqueue(s1.pop())

assert(findKey(20)==True)
assert(findKey(200)==False)