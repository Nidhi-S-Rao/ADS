from singlyLinkedList import *

#Reverse the single linked list
def reverse(s1):
    cur=s1.head
    prev=None
    s1.tail=cur
    while cur:
        next=cur.next
        cur.next=prev
        prev=cur
        cur=next
        s1.head=prev
    return (s1.getElements())
    

s1=SList()
for i in range(1,8):
    s1.addAtTail(i)
assert(reverse(s1)==([7, 6, 5, 4, 3, 2, 1]))

