#Program to get max element in singly linked list with time complexity O(1). No deletions allowed
class SList:
    class Node:
        def __init__(self,ele):
            self.data=ele
            self.next=None
    def __init__(self):
            self.head=None
            self.tail=None
            self.count=0
            self.max=0
    def isEmpty(self):
        return self.count==0
    def listCount(self):
        return self.count
    def maxElement(self):
        return self.max
    def addAtHead(self,ele):
        new_node=self.Node(ele)
        if not self.isEmpty():
            new_node.next=self.head
            self.head=new_node
        else:
            self.head=self.tail=new_node
        self.count+=1
        if(new_node.data>self.max):
            self.max=new_node.data
        return self.count
    def addAtTail(self,ele):
        new_node=self.Node(ele)
        if not self.isEmpty():
            self.tail.next=new_node
            self.tail=new_node
        else:
            self.head=self.tail=new_node
        self.count+=1
        if(new_node.data>self.max):
            self.max=new_node.data
        return self.count



slist=SList()
slist.addAtHead(10)
assert(slist.maxElement()==10)
slist.addAtTail(20)
slist.addAtHead(5)
assert(slist.maxElement()==20)