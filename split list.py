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

    def split(self,obj1,obj2):
        current=self.head
        obj1.head=Node(current.data)
        obj1.lastnode=obj1.head
        current=current.next
        obj2.head=Node(current.data)
        obj2.lastnode=obj2.head
        current=current.next

        while current is not None:
              temp=Node(current.data)
              obj1.lastnode.next=temp
              obj1.lastnode=temp
              if current is None:
                  return
              current=current.next
              temp=Node(current.data)
              obj2.lastnode.next=temp
              obj2.lastnode=temp
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
obj2=LinkedList()
n=int(input("How many elements you wants to enter :"))
for i in range(n):
    data=int(input("Enter data "))
    obj.at_end(data)
obj.split(obj1,obj2)
print("Obj1 list :")
obj1.display()
print("Obj2 list :")
obj2.display()
