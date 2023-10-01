class CList:
    class Node:
        def __init__(self,ele):
            self.data=ele
            self.next=None
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0

    def isEmpty(self):
        return self.count==0
    
    def getCount(self):
        return self.count
    
    def addAtHead(self,ele):
        new_node=self.Node(ele)
        if not self.isEmpty():
            self.tail.next=new_node
            new_node.next=self.head
            self.head=new_node
        else:
            self.head=self.tail=new_node
            self.tail.next=self.head
        self.count+=1
        return self.count
    
    def addAtTail(self,ele):
        new_node=self.Node(ele)
        if not self.isEmpty():
            self.tail.next=new_node
            new_node.next=self.head
            self.tail=new_node
        else:
            self.head=self.tail=new_node
            self.tail.next=self.head
        self.count+=1
        return self.count
    
    def deleteAtHead(self):
        if not self.isEmpty():
            ele=self.head.data
            temp=self.head.next
            if(temp!=self.tail):
                self.tail.next=temp
                self.head=temp
            else:
                self.head=self.tail
            self.count-=1
            return ele
        else:
            print("None")
            return None
    
    def deleteAtTail(self):
        if not self.isEmpty():
            ele=self.tail.data
            cur=self.head
            while(cur.next!=self.tail):
                cur=cur.next
            cur.next=self.head
            self.tail=cur
            self.count-=1
            return ele
        else:
            print("None")
            return None
    
    def getElements(self):
        if not self.isEmpty():
            cur=self.head.next
            l=[]
            l.append(self.head.data)
            while(cur!=self.head):
                l.append(cur.data)
                cur=cur.next
            return l
        else:
            return None
        
clist=CList()
assert(clist.addAtHead(10)==1)
assert(clist.addAtTail(20)==2)
assert(clist.addAtHead(5)==3)
assert(clist.addAtTail(25)==4)
assert(clist.getElements()==[5, 10, 20, 25])
assert(clist.deleteAtHead()==5)
assert(clist.deleteAtTail()==25)
assert(clist.getElements()==[10, 20])
assert(clist.deleteAtTail()==20)
assert(clist.deleteAtTail()==10)
assert(clist.addAtHead(10)==1)
assert(clist.addAtTail(20)==2)
assert(clist.deleteAtHead()==10)
assert(clist.deleteAtHead()==20)
