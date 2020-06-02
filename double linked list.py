class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

class Linkedlist:
    def __init__(self):
        self.head=None
        self.lastnode=None
        self.tail=None

    def append(self,data):
        if self.head is None:
            self.head=Node(data)
            self.lastnode=self.head
        else:
            temp=Node(data)
            temp.prev=self.lastnode
            self.lastnode.next=temp
            self.lastnode=temp

    def insert_at_begin(self,data):
        if self.head is None:
            self.head=Node(data)
            self.lastnode=self.head
        else:
            temp=Node(data)
            temp.next=self.head
            self.head.prev=temp
            self.head=temp
            temp.prev=None

    def delete_begin(self):
        if self.head is None:
            print("List is empty")
        else:
            temp=self.head
            self.head=temp.next
            self.head.prev=None
            temp=None

    def delete_last(self):
        if self.head is None:
            print("List is empty")
        if(self.head==self.lastnode):
            print("Removed data",self.head.data)
            self.head=None
            self.lastnode=None
        else:
           print("Removed data",self.lastnode.data)
           temp=self.lastnode
           self.lastnode=self.lastnode.prev
           self.lastnode.next=None
           temp=None

    def display(self):
        if self.head is None:
            print("List is empty ")
        else:
            current=self.head
            while current is not None:
                print(current.data)
                current=current.next
obj=Linkedlist()
n=int(input("How many elements you wants to enter :"))
for i in range(n):
    data=int(input("Enter data "))
    obj.append(data)
obj.display()
n=int(input("How many elements you wants to enter :"))
for i in range(n):
    data=int(input("Enter data "))
    obj.insert_at_begin(data)
print("Elements enter at strat ")
obj.display()
print("Element deleted present at start : ")
obj.delete_begin()
obj.display()
print("Element deleted present at end : ")
obj.delete_last()
obj.display()
