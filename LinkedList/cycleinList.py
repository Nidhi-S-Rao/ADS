class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

def has_cycle(head):
    if not head:
        return False
    
    # Initialize the two pointers
    cur=head
    next=head


    while cur.next and next.next.next:
       cur=cur.next
       next=next.next.next
       if cur==next:
            # If the two pointers meet, there's a cycle
            return True

    # If we reach the end of the list without meeting, there's no cycle
    return False


node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2

assert(has_cycle(node1)==True)