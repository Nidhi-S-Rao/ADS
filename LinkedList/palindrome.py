from singlyLinkedList import *
from reverse import *

#Check whether given linked list is palindrome or not.
def palindrome(s1):
    return s1.getElements()==reverse(s1)
  
    

s1=SList()
for i in range(1,8):
    s1.addAtTail(i)
assert(palindrome(s1)==False)
s2=SList()
s2.addAtTail('M')
s2.addAtTail('A')
s2.addAtTail('L')
s2.addAtTail('A')
s2.addAtTail('Y')
s2.addAtTail('A')
s2.addAtTail('L')
s2.addAtTail('A')
s2.addAtTail('M')
assert(palindrome(s2)==True)

