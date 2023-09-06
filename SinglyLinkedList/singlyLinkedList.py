#Implementation of Singly Linked List
class SList:
    #Creating a node
    class Node:
        def __init__(self,ele):
            self.data=ele
            self.next=None
            #Initializing the head and tail information
        def __init__(self):
            self.head=None
            self.tail=None
            self.count=0
            self.max=0
        #Checking if the list is empty
        def isEmpty(self):
            return self.count==0
        #Getting the count of nodes in the list
        def listCount(self):
            return self.count
        #Adding a node at head
        def addAtHead(self,ele):
            new_node=self.Node(ele)
            if not self.isEmpty():
                new_node.next=self.head
                self.head=new_node
            else:
                self.head=self.tail=new_node
            self.count+=1
            return self.count
        #Adding a new node at tail of the list
        def addAtTail(self,ele):
            new_node=self.Node(ele)
            if not self.isEmpty():
                self.tail.next=new_node
                self.tail=new_node
            else:
                self.head=self.tail=new_node
            self.count+=1
            return self.count
        #Deleting a node at head of the list
        def deleteAtHead(self):
            if not self.isEmpty():
                data=self.head.data
                self.head=self.head.next
                if(self.head==None):
                    self.tail=None
                self.count-=1
                return data
            else:
                return None
        #Deleting a node at tail of the list
        def deleteAtTail(self):
            if not self.isEmpty():
                if(self.count!=1):
                    last=self.tail
                    cur=self.head
                    while(cur.next!=last):
                        cur=cur.next
                    self.tail=cur
                    cur.next=None
                else:
                    self.head=self.tail=None
                self.count-=1
            else:
                return None
        #Checking if a given key present in the linked list
        def isMemeber(self,key):
            if not self.isEmpty():
                cur=self.head
                while(cur!=None):
                    if(cur==key):
                        break
                    else:
                        cur=cur.next
                return cur!=None
            else:
                return None

