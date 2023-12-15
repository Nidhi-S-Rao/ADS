class BinaryTree:
    class _node:
        def __init__(self,id):
            self.data=id
            self.left=None
            self.right=None
    def __init__(self):
        self.count=0
        self.root=None
    def addElement(self,ele):
        cur=self.root
        node=self._node(ele)
        c=self._addElement(cur,node)
        return c
    def _addElement(self,temp,node):
        cur=temp
        if(cur==None):
            print("Root")
            self.root=node
            self.count+=1
        else:
            if(cur.left==None):
                print("Added to left")
                cur.left=node
                self.count+=1
            elif(cur.right==None):
                print("Added to right")
                cur.right=node
                self.count+=1
            else:
                if(cur.left):
                    print("Left tree traversal",cur.left.data)
                    self._addElement(cur.left,node)
                else:
                    print("Right tree traversal",cur.right.data)
                    self._addElement(cur.right,node)
        return(self.count)
        
    def inOrder(self):
        self._inOrder(self.root)
    def _inOrder(self,node):
        if node!=None:
            self._inOrder(node.left)
            print(node.data)
            self._inOrder(node.right)



bt=BinaryTree()
print(bt.addElement(10))
print(bt.addElement(20))
print(bt.addElement(30))
print(bt.addElement(40))
print(bt.addElement(50))
#print(bt.addElement(60))

bt.inOrder()