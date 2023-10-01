from singlyLinkedList import *

"""Assume that we have two linked lists. Elements in individual list are unique. There may 
be identical elements across linked lists. Create a third list which contains only common 
elements across first two lists"""

def check(s1,s2,s3):
    sList1=[]
    sList2=[]
    cur1=s1.head
    cur2=s2.head
    while(cur1!=None):
        sList1.append(cur1.data)
        cur1=cur1.next
    while(cur2!=None):
        sList2.append(cur2.data)
        cur2=cur2.next
    for i in sList1:
        if i in sList2:
            s3.addAtTail(i)
    return s3.getElements()
    
    

s1=SList()
s2=SList()
s3=SList()
for i in range(1,7):
    s1.addAtTail(i)
for i in range(4,12):
    s2.addAtHead(i)
assert(check(s1,s2,s3)==([4,5,6]))