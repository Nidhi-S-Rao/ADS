class DhanaLakshmi:
    class Share:
        def __init__(self,name,price,units):
            self.name=name
            self.price=price
            self.units=units
            self.next=None
            
        
    def __init__(self):
        self.head=None
        self.tail=None
        self.count=0
    def addShare(self,name,price,units):
        if self.count>=5:
            share=self.head
            last=share.next
            self.head=last
            self.estimation(share.name,share.price,share.units)
        new_share=self.Share(name,price,units)
        node=self.tail
        if node==None:
            self.head=self.tail=new_share
        else:
            node.next=new_share
            self.tail=new_share 
        self.count+=1
    def estimation(self,name,price,units):
        n=int(input("Enter current price for share "+name+" : "))
        old_value=price*units
        new_value=n*units
        if(old_value>new_value):
            print("There is a loss of "+str((new_value-old_value)*-1))
        if(old_value<new_value):
            print("There is a profit of "+str(new_value-old_value))

    def getCount(self):
        return self.count
dhan=DhanaLakshmi()
dhan.addShare('A',20,3)
dhan.addShare('B',10,2)
dhan.addShare('C',5,4)
dhan.addShare('D',30,2)
dhan.addShare('E',40,1)
print(dhan.getCount())
dhan.addShare('F',50,2)
dhan.addShare('G',50,2)



    