from singlyLinkedList import *

#Find the sum of last ‘n’ nodes in single linked list. Where ‘n’ will be given. Sum should be calculated with one iteration.
def sum(s1,n):
    k=s1.listCount()-n+1
    cur=s1.head
    count=1
    while(count<k):
        cur=cur.next
        count+=1
    sum=0
    while(cur!=None):
        sum=sum+cur.data
        if(cur!=None):
            cur=cur.next
    return sum

s1=SList()
s2=SList()
for i in range(1,8):
    s1.addAtTail(i)
assert(sum(s1,4)==22)
for i in range(4,12):
    s2.addAtHead(i)
assert(sum(s2,5)==30)

