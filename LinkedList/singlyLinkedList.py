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
        return self.head.data,self.tail.data
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
            if(self.count>=1):
                last=self.tail
                cur=self.head
                while(cur.next!=last):
                    cur=cur.next
                self.tail=cur
                
                cur.next=None
            else:
                self.head=self.tail=None
            self.count-=1
            return last.data
        else:
            return None
    #Checking if a given key present in the linked list
    def isMemeber(self,key):
        if not self.isEmpty():
            cur=self.head
            while(cur!=None):
                if(cur.data==key):
                    break
                else:
                    cur=cur.next
            return cur!=None
        else:
            return None
    #Adding a node after a given node
    def addAfterNode(self,key,ele):
        new_node=self.Node(ele)
        if not self.isEmpty():
            cur=prev=self.head
            while(cur!=None):
                if(cur.data==key):
                    prev=cur
                    if(cur.next!=None):
                        cur=cur.next
                        prev.next=new_node
                        new_node.next=cur
                        self.count+=1
                        break
                    else:
                        cur.next=new_node
                        self.tail=new_node
                        self.count+=1
                        break
                else:
                    cur=cur.next
        else:                   
            self.head=self.tail==new_node
            self.count+=1
        return self.count
    
    #Adding a node at given poition
    def addAtPos(self,ele,n):
        new_node=self.Node(ele)
        count=1
        if not self.isEmpty():
            cur=self.head
            while(count<n):
                prev=cur
                if(cur!=None):
                    cur=cur.next
                    count+=1
            if(n<=self.count and n!=1):
                prev.next=new_node
                new_node.next=cur
                self.count+=1
            elif(n==1):
                new_node.next=self.head
                self.head=new_node
                self.count+=1
        else:
            self.head=self.tail=new_node
            self.count+=1
        return self.count
            



    
    #Adding a node before a given node
    def addBeforeNode(self,key,ele):
        new_node=self.Node(ele)
        if not self.isEmpty():
            cur=prev=self.head
            while(cur!=None):
                if(cur.data==key):
                    if(cur!=self.head):
                        prev.next=new_node
                        new_node.next=cur
                        self.count+=1
                        break
                    else:
                        new_node.next=cur
                        self.head=new_node
                        self.count+=1
                        break
                else:
                    prev=cur
                    cur=cur.next
        else:                   
            self.head=self.tail==new_node
            self.count+=1
        return self.count
    
            
    #Deleting a node after a given node
    def deleteAfterNode(self,key):
        if not self.isEmpty():
            cur=self.head
            while(cur!=None):
                if(cur.data==key):
                    temp=cur.next
                    if(temp!=None):
                        next=temp.next
                        if(next!=None):
                            cur.next=next
                            self.count-=1
                            break
                        else:
                            cur.next=None
                            self.tail=cur
                            self.count-=1
                            break
                    else:
                        return None
                        
                else:
                    cur=cur.next
        else:                   
            return None
        
        return temp.data
    
    #Delete a node given position
    def deleteAtPos(self,pos):
        if not self.isEmpty():
            cur=self.head
            last=self.tail
            count=1
            if(pos<=self.count):
                while(count<pos):
                    prev=cur
                    cur=cur.next
                    count+=1
                if(cur==self.head):
                    self.head=cur.next
                    self.count-=1
                elif(cur!=last):
                    temp=cur.next
                    prev.next=temp
                    self.count-=1
                elif(cur==last):
                    prev.next=None
                    self.tail=prev
                    self.count-=1
                return cur.data
            else:
                return None
        else:
            return None
            
    #Deleting a given node
    def deleteNode(self,key):
        if not self.isEmpty():
            cur=self.head
            
            while(cur!=None):
                
                if(cur.data==key):
                    if(cur==self.tail):
                        prev.next=None
                        self.tail=prev
                        self.count-=1
                        break
                    elif(cur==self.head):
                        self.head=self.head.next
                        self.count-=1
                        break
                    else:
                        temp=cur.next
                        prev.next=temp
                        self.count-=1
                        break
                else:
                    prev=cur
                    cur=cur.next
            return cur.data
        else:
            return None
        
    #Deleting a node before a given node
    def deleteBeforeNode(self,key):
        if not self.isEmpty():
            cur=prev=self.head
            while(cur!=None and cur.data!=key):
                before=prev
                prev=cur
                cur=cur.next
            if(cur!=None):
                if(cur!=self.head and prev!=self.head):
                    before.next=cur
                    self.count-=1
                    return prev.data
                elif(cur!=self.head and prev==self.head):
                    self.head=cur
                    self.count-=1
                    return prev.data
            else:
                return None
        else:                   
            return None
        

    #Printing all the elements
    def getElements(self):
        list=[]
        if not self.isEmpty():
            cur=self.head
            while(cur!=None):
                list.append(cur.data)
                cur=cur.next
            return list

slist=SList()
slist.addAtHead(10)
slist.addAtTail(20)
slist.addAtHead(5)
slist.addAfterNode(10,15)
assert(slist.getElements()==([5,10,15,20]))
slist.addAfterNode(20,25)
assert(slist.getElements()==([5,10,15,20,25]))
assert(slist.deleteAtHead()==5)
assert(slist.deleteAtTail()==25)
assert(slist.getElements()==([10,15,20]))
slist.addAtHead(5)
assert(slist.addAfterNode(20,25)==5)
assert(slist.getElements()==([5,10,15,20,25]))
assert(slist.deleteAfterNode(10)==15)
assert(slist.deleteAfterNode(20)==25)
assert(slist.deleteAfterNode(20)==None)
assert(slist.isMemeber(10)==True)
slist.addAtTail(30)
assert(slist.getElements()==([5, 10, 20, 30]))
slist.addBeforeNode(30,25)
assert(slist.getElements()==([5, 10, 20, 25, 30]))
slist.addBeforeNode(5,1)
assert(slist.getElements()==([1,5, 10, 20, 25, 30]))
assert(slist.addBeforeNode(2,0)==6)
assert(slist.getElements()==([1,5, 10, 20, 25, 30]))
assert(slist.addAtPos(0,1)==7)
assert(slist.getElements()==([0,1,5, 10, 20, 25, 30]))
assert(slist.addAtPos(28,7)==8)
assert(slist.getElements()==([0,1,5, 10, 20, 25,28, 30]))
assert(slist.addAtPos(35,9)==8)
assert(slist.addAtPos(15,5)==9)
assert(slist.getElements()==([0,1,5, 10, 15,20, 25,28, 30]))
assert(slist.deleteAtPos(1)==0)
assert(slist.getElements()==([1,5, 10, 15,20, 25,28, 30]))
assert(slist.deleteAtPos(8)==30)
assert(slist.getElements()==([1,5, 10, 15,20, 25,28]))
assert(slist.deleteAtPos(4)==15)
assert(slist.getElements()==([1,5, 10,20, 25,28]))
assert(slist.deleteAtPos(10)==None)
assert(slist.deleteNode(5)==5)
assert(slist.getElements()==([1,10,20, 25,28]))
assert(slist.deleteNode(1)==1)
assert(slist.getElements()==([10,20, 25,28]))
assert(slist.deleteNode(28)==28)
assert(slist.getElements()==([10,20, 25]))
assert(slist.deleteBeforeNode(10)==None)
assert(slist.getElements()==([10,20, 25]))
slist.addAtHead(5)
slist.addAfterNode(10,15)
assert(slist.getElements()==([5,10,15,20, 25]))
assert(slist.deleteBeforeNode(15)==10)
assert(slist.getElements()==([5,15,20, 25]))
assert(slist.deleteBeforeNode(25)==20)
assert(slist.getElements()==([5,15, 25]))
assert(slist.deleteBeforeNode(30)==None)
assert(slist.deleteBeforeNode(15)==5)
assert(slist.getElements()==([15, 25]))
assert(slist.deleteBeforeNode(25)==15)
assert(slist.deleteAtHead()==25)
