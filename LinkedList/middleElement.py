from singlyLinkedList import *

#Find middle element of linked list without iterating all elements
def middleElement(s1):
    k=s1.listCount()/2
    cur=s1.head
    count=1
    while(count<k):
        cur=cur.next
        count+=1
    if(k%2==0):
        return cur.data,cur.next.data
    else:
        return cur.data

s1=SList()
s2=SList()
for i in range(1,8):
    s1.addAtTail(i)
assert(middleElement(s1)==4)
for i in range(4,12):
    s2.addAtHead(i)
assert(middleElement(s2)==(8,7))

