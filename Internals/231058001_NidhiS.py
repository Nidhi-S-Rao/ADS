#Using doubly linked list
class Shop:
    class items:
        def __init__(self,item,code,quantity):
            self.item_code=code
            self.item_name=item
            self.item_count=0
            self.quantity_sold=0
            self.quantity_available=quantity
            self.next=None
            self.prev=None
    def __init__(self):
        self.head=None
        self.count=0
        self.max=0
        self.min=99999999
        self.Maxitem=None
        self.minItem=None
    def addItems(self,item,code,quantity):
        new_item=self.items(item,code,quantity)
        temp=self.head
        if(temp==None):
            self.head=new_item
            self.count+=1
        else:
            while(temp.next!=None):
                if(temp.item_name==item):
                    temp.quantity_available=temp.quantity_available+quantity
                    break
                else:
                    temp=temp.next
            if(temp.next==None):
                new_item=self.items(item,code,quantity)
                temp.next=new_item
                new_item.prev=temp
                self.count+=1
        
        return self.count
    def searchItem(self,key,quantity):
        if not self.count==0:
            cur=self.head
            while(cur!=None):
                if(cur.item_name==key and cur.quantity_available>0):
                    cur.item_count+=1
                    cur.quantity_sold=cur.quantity_sold+quantity
                    cur.quantity_available=cur.quantity_available-quantity
                    break
                else:
                    cur=cur.next
            if(cur!=None):
                print("The item ", key, " added to your cart")
            else:
                print("Sorry this item is not available in the store at this moment")
    def getItemsList(self):
        if not self.count==0:
            items_list=[]
            cur=self.head
            while(cur!=None):
                items_list.append(cur.item_name)
                cur=cur.next
            return items_list
        
    def fastMovingItems(self):
        if not self.count==0:
            cur=self.head
            while(cur!=None):
                data=cur.item_count
                if(data>self.max):
                    self.max=data
                    self.Maxitem=cur.item_name
                cur=cur.next
            return self.Maxitem
    def slowMovingItems(self):
        if not self.count==0:
            cur=self.head
            while(cur!=None):
                data=cur.item_count
                if(data<self.min):
                    self.min=data
                    self.minItem=cur.item_name
                cur=cur.next
            return self.minItem
        
    def getQuantity(self,code):
        cur=self.head
        while(cur!=None):
            if(cur.item_code==code):
                quantity=cur.quantity_sold
                break
            else:
                cur=cur.next
        if(cur!=None):
            print("Total ", quantity," quantity of items with code ",code," has been sold")
        else:
            print("not able to find the product with that item code")

    def getAvailableQuantity(self,code):
        cur=self.head
        while(cur!=None):
            if(cur.item_code==code):
                quantity=cur.quantity_available
                break
            else:
                cur=cur.next
        if(cur!=None):
            print("Total ", quantity," quantity of items with code ",code," is available")
        else:
            print("not able to find the product with that item code")

    
    

        



"""s1=Shop()
s1.addItems("Goodday",1)
s1.addItems("Hide&Seek",2)
s1.addItems("Lays",3)
s1.addItems("Kurkure",4)
s1.addItems("50-50",5)
s1.addItems("Doritos",6)
print(s1.getItemsList())
s1.searchItem("Goodday",2)
s1.searchItem("Hide&Seek",5)
s1.searchItem("Lays",4)
s1.searchItem("Lays",4)
s1.searchItem("Goodday",2)
s1.searchItem("Goodday",2)
print(s1.fastMovingItems())
print(s1.slowMovingItems())
s1.getQuantity(1)"""

def mainFunction():
    s1=Shop()
    s1.addItems("Goodday",1,50)
    s1.addItems("Hide&Seek",2,40)
    s1.addItems("Lays",3,4)
    s1.addItems("Kurkure",4,35)
    s1.addItems("50-50",5,25)
    s1.addItems("Doritos",6,60)
    s1.addItems("Goodday",1,50)
    print(s1.getItemsList())
    while(True):
        option=int(input("Please select an option:1.Add to cart, 2. get fast moving item 3. get slow moving items, 4. get quantity of an item , 5. Get available quantity"))
        if(option==1):
            print("Hello Welcome to the store. These are the available items at our store. Please enter items to add it to your cart. Thank You")
            items=input("Please enter your items:")
            quantity=input("Please enter the quantity:")
            items_list=items.split(',')
            quantity_list=quantity.split(',')
            print(items_list,quantity_list)
            if (len(items_list)==len(quantity_list)):
                for i in range(len(items_list)):
                    s1.searchItem(items_list[i],int(quantity_list[i]))
        if(option==2):
            print(s1.fastMovingItems())
        if(option==3):
            print(s1.slowMovingItems())
        if(option==4):
            n=(input("Please enter the item code:"))
            s1.getQuantity(int(n))
        if(option==5):
            n=(input("Please enter the item code:"))
            s1.getAvailableQuantity(int(n))

    
    
    




mainFunction()
