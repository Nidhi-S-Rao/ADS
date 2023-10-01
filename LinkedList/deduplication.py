from singlyLinkedList import *

#Write an efficient code to remove duplicate elements from single linked list
def deDuplicate(s1):
    cur=prev=s1.head
    s=[]
    while cur!=None:
        if cur.data in s:
            prev.next=cur.next
            cur=cur.next
        else:
            s.append(cur.data)
            prev=cur
            cur=cur.next
    return s1.getElements()




s1=SList()
s2=SList()
for i in range(1,9):
    s1.addAtTail(i)
assert(deDuplicate(s1)==([1, 2, 3, 4, 5, 6, 7, 8]))
for i in range(1,9):
    s2.addAtTail(i)
for i in range(7,13):
    s2.addAtTail(i)
for i in range(5,9):
    s2.addAtHead(i)
assert(deDuplicate(s2)==([8, 7, 6, 5, 1, 2, 3, 4, 9, 10, 11, 12]))