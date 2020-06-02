def binarySearch(list1,n,key):
    start=0
    end=n
    mid=(start+end)//2
    while(start<=end):
        if(list1[mid]==key):
            return mid
        elif(key<list1[mid]):
            end=mid-1
        else:
            start=mid+1
    return -1

list1=[10,20,30,40,50,60]
key=30
n=len(list1)-1
item=binarySearch(list1,n,key)
if(item!=-1):
    print("ELement present in list",item)
else:
    print("ELement not present in list")
