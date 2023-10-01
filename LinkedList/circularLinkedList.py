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
                self.tail=self.head
            self.count-=1
            return ele
        else:
            print("None")
            return None
    
    def deleteAtTail(self):
        if not self.isEmpty():
            ele=self.tail.data
            cur=self.head
            while(cur!=self.tail):
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
        
dlist=CList()
assert(dlist.addAtHead(10)==1)
assert(dlist.addAtTail(20)==2)
assert(dlist.addAtHead(5)==3)
assert(dlist.addAtTail(25)==4)
assert(dlist.getElements()==[5, 10, 20, 25])
assert(dlist.deleteAtHead()==5)
assert(dlist.deleteAtTail()==25)
assert(dlist.getElements()==[10, 20, 25])
assert(dlist.deleteAtHead()==10)
assert(dlist.deleteAtHead()==20)
print(dlist.getCount())