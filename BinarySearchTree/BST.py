from simpleQueue import *
class BST:
    class _Node:
        def __init__(self,ele):
            self.data=ele
            self.left=None
            self.right=None
    def __init__(self):
        self.root=None
        self.count=0
    def isEmpty(self):
        return self.count==0
    def getCount(self):
        return self.count
    def addNode(self,ele):
        cur=parent=self.root
        while(cur!=None and cur.data!=ele):
            parent=cur
            if(ele<cur.data):
                cur=cur.left
            else:
                cur=cur.right
        if(cur==None):
            new_node=self._Node(ele)
            if(parent==None):
                self.root=new_node
            else:
                if(ele<parent.data):
                    parent.left=new_node
                else:
                    parent.right=new_node
            self.count+=1
        return self.count
    def searchNode(self,ele):
        if not self.isEmpty():
            cur=self.root
            while(cur!=None):
                if(cur.data==ele):
                    break
                else:
                    if(cur.data>ele):
                        cur=cur.left
                    else:
                        cur=cur.right
            return cur!=None
        else:
            return False
        
    #Traversal
    #Inorder Traversal
    def InOrder(self):
        a=[]
        if not self.isEmpty():
            self._inOrder(self.root,a)
        return a
    def _inOrder(self,node,l):
        if node!=None:
            self._inOrder(node.left,l)
            l.append(node.data)
            self._inOrder(node.right,l)
    
    
    #Preorder Traversal
    def PreOrder(self):
        a=[]
        if not self.isEmpty():
            self._preOrder(self.root,a)
        return a
    def _preOrder(self,node,l):
        if node!=None:
            l.append(node.data)
            self._preOrder(node.left,l)
            self._preOrder(node.right,l)
        
    
    #Postorder Traversal
    def PostOrder(self):
        a=[]
        if not self.isEmpty():
            self._postOrder(self.root,a)
        return a
    def _postOrder(self,node,l):
        if node!=None:
            self._postOrder(node.left,l)
            self._postOrder(node.right,l)
            l.append(node.data)
        
        
    #Levelorder Traversal
    def LevelOrder(self):
        if not self.isEmpty():
            l=[]
            q1=SimpleQueue()
            q1.enqueue(self.root)
            while not q1.isQueueEmpty():
                node=q1.dequeue()
                l.append(node.data)
                if node.left:
                    q1.enqueue(node.left)
                if node.right:
                    q1.enqueue(node.right)
            return l
        else:
            return None
        
    def getLeafCount(self):
        if not self.isEmpty():
            return(self._leafCount(self.root))
        else:
            return 0
    def _leafCount(self,node):
        if node:
            if self.isLeafNode(node):
                return 1
            else:
                return(self._leafCount(node.left)+self._leafCount(node.right))
        else:
            return 0
    def isLeafNode(self, node):
        if node.left==None and node.right==None:
            return True
        else:
            return False
        
#To traverse in descending order in a BST
    def traverseDescendingOrder(self):
        a=[]
        if not self.isEmpty():
            self.descendingOrder(self.root,a)
            return a
    def descendingOrder(self,node,a):
        if node:
            self.descendingOrder(node.right,a)
            a.append(node.data)
            self.descendingOrder(node.left,a)

#To get the height of a binary search tree
    def getHeight(self):
        if not self.isEmpty():
            return(self._getHeight(self.root)+1)
    
    def _getHeight(self,node):
        if node.right and node.left:
            return max(self._getHeight(node.left),self._getHeight(node.right))
        else:
            if node.right:
                return self._getHeight(node.right)+1
            elif node.left:
                return self._getHeight(node.left)+1
            else:
                return 1
            
        

    def deleteNode(self,key):
        if not self.isEmpty():
            self.root=self._nodeDelete(self.root,key)
            return self.count
        else:
            return None
    def _nodeDelete(self,node,key):
        if node==None:
            return None
        elif key<node.data:
            node.left=self._nodeDelete(node.left,key)
        elif key>node.data:
            node.right=self._nodeDelete(node.right,key)
        else:
            if node.left and node.right:
                temp=self._findMin(node.right)
                node.data=temp.data
                node.right=self._nodeDelete(node.right,temp.data)
            else:
                if node.right==None:
                    node=node.left
                    self.count-=1
                else:
                    node=node.right
                    self.count-=1
            
        return node
    def _findMin(self,node):
        if node.left==None:
            return node
        else:
            return self._findMin(node.left)







bst=BST()
assert(bst.addNode(45)==1)
assert(bst.addNode(30)==2)
assert(bst.addNode(50)==3)
assert(bst.addNode(25)==4)
assert(bst.addNode(40)==5)
assert(bst.addNode(60)==6)
assert(bst.addNode(55)==7)
assert(bst.getCount()==7)
assert(bst.searchNode(25)==True)
assert(bst.searchNode(80)==False)
assert(bst.InOrder()==([25, 30, 40, 45, 50, 55, 60]))
assert(bst.PreOrder()==([45, 30, 25, 40, 50, 60, 55]))
assert(bst.PostOrder()==([25, 40, 30, 55, 60, 50, 45]))
assert(bst.LevelOrder()==([45, 30, 50, 25, 40, 60, 55]))
assert(bst.getLeafCount()==3)
assert(bst.traverseDescendingOrder()==([60, 55, 50, 45, 40, 30, 25]))
assert(bst.getHeight()==4)
assert(bst.deleteNode(40)==6)
assert(bst.PreOrder()==([45, 30, 25, 50, 60, 55]))
assert(bst.deleteNode(25)==5)
assert(bst.traverseDescendingOrder()==([60, 55, 50, 45,30]))
assert(bst.InOrder()==([30, 45, 50, 55, 60]))
assert(bst.deleteNode(45)==4)
assert(bst.PostOrder()==([30, 55, 60, 50]))
assert(bst.getHeight()==3)
assert(bst.addNode(52)==5)
assert(bst.addNode(40)==6)
assert(bst.addNode(35)==7)
assert(bst.addNode(38)==8)
assert(bst.getHeight()==5)
assert(bst.getLeafCount()==2)