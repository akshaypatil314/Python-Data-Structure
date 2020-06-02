class sta:
    def __init__(self):
        self.stack=list()
        self.top=0
        self.maxsize=4

    def insert(self,data):
        if(self.top>=self.maxsize):
            print("Stack is Full")
        else:
            self.stack.append(data)
            self.top+=1

    def delete(self):
        if(self.top<=0):
            print("Stack is empty ")
        else:
            item=self.stack.pop()
            self.top-=1
            return(item)
    def display(self):
        print(self.stack)

obj=sta()
choice=1
while(choice!=0):
    print("1.Insert into Stack")
    print("2.Remove from Stack")
    print("3.Display Stack")
    print("4.Exit")

    choice=int(input("Enter choice : "))
    if(choice==1):
        data=int(input("Enter data to insert : "))
        obj.insert(data)
    elif(choice==2):
        print(obj.delete())
    elif(choice==3):
        obj.display()
    else:
        exit()
