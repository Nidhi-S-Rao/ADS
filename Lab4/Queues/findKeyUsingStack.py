from stack import *;
from simpleQueue import*;
#Program to check if key is present in the given stack using 2 stacks
def findKey(key):
    s1=stack()
    s2=stack()
    s1.push(10)
    s1.push(20)
    s1.push(30)
    s1.push(40)
    f=0
    while(s1.count>0):
        ele=s1.pop()
        s2.push(ele)
        if(key==ele):
            f=1
    while(s2.count>0):
        s1.push(s2.pop())
    return f==1
assert(findKey(20)==True)
assert(findKey(100)==False)