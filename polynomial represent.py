class Node:
    def __init__(self,coeff,expo):
        self.coeff=coeff
        self.expo=expo
        self.next=None

class List:
    def __init__(self):
        self.head=None
        self.lastnode=None

    def append(self,coeff,expo):
        if self.head is None:
            self.head=Node(coeff,expo)
            self.lastnode=self.head
        else:
            temp=Node(coeff,expo)
            self.lastnode.next=temp
            self.lastnode=temp

    def display(self):
        if self.head is None:
            print("List is empty ")
        else:
            current=self.head
            while current is not None:
                if(current.expo==0):
                    print("%dx"%(current.coeff))
                else:
                    print("%dx^%d+"%(current.coeff,current.expo)," ")
                current=current.next

obj=List()
n=int(input("How many elements wants to enter : "))
for i in range(n):
    coeff=int(input("Enter Coefficent : "))
    expo=int(input("Enter Exponent : "))
    obj.append(coeff,expo)
obj.display()
