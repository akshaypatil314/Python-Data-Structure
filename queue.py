class que:
    def __init__(self):
        self.queue=[]
        self.maxsize=3
        self.front=-1
        self.rear=-1

    def enqueue(self,data):
        if(self.rear==self.maxsize-1):
            print("Queue is full")
        else:
            self.rear+=1
            self.queue.append(data)
            print("Added succesfully")

    def dequeue(self):
        if(self.rear==-1 and self.front==-1):
            print("Queue is empty")
        elif(self.rear==self.front):
            self.rear=-1
            self.front=-1
        else:
            item=self.queue.pop(0)
            self.front+=1
            return item

    def display(self):
        print(self.queue)


obj=que()
choice=1
while(choice!=0):
    print("1.Insert into Queue")
    print("2.Remove from Queue")
    print("3.Display Queue")
    print("4.Exit")

    choice=int(input("Enter choice : "))
    if(choice==1):
        data=int(input("Enter data to insert : "))
        obj.enqueue(data)
    elif(choice==2):
        print(obj.dequeue())
    elif(choice==3):
        obj.display()
    else:
        exit()
