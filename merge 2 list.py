class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
        self.lastnode=None

    def at_end(self,data):
        if self.head is None:
            self.head=Node(data)
            self.lastnode=self.head
        else:
            temp=Node(data)
            self.lastnode.next=temp
            self.lastnode=temp

    def merge(self,obj1):
        self.lastnode.next=obj1.head


    def clone(self,obj):
        self.head=Node(obj.head.data)
        self.lastnode=self.head
        current=obj.head
        current=current.next

        while current is not None:
            temp=Node(current.data)
            self.lastnode.next=temp
            self.lastnode=temp
            current=current.next
        
    
    def display(self):
        if self.head is None:
            print("List is empty ")
        else:
            current=self.head
            while current is not None:
                print(current.data)
                current=current.next

obj=LinkedList()
obj1=LinkedList()
n=int(input("How many elements you wants to enter :"))
for i in range(n):
    data=int(input("Enter data "))
    obj.at_end(data)
obj.display()
n=int(input("How many elements you wants to enter :"))
for i in range(n):
    data=int(input("Enter data "))
    obj1.at_end(data)
obj1.display()
print("After Merging :")
obj.merge(obj1)
obj.display()
print("After Cloning :")
obj2=LinkedList()
obj2.clone(obj)
obj2.display()
