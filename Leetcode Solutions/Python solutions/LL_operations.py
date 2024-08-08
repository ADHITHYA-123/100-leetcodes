class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist():
    def __init__(self):
        self.head=None
    
    def insert_back(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            return
        last=self.head
        while last.next:
            last=last.next
        last.next=newnode 

    def insert_front(self,data):
        newnode=Node(data)
        newnode.next=self.head
        self.head=newnode

    def insert_pos(self,data,pos):
        if pos<0:
            print("Invalid position!")
            return
        newnode=Node(data)
        if pos==0:
            newnode=Node(data)
            newnode.next=self.head
            self.head=newnode
            return
        current=self.head
        for _ in range(pos-1):
            if not current:
                print("Position out of bound")
                return
            current=current.next
        newnode.next=current.next
        current.next=newnode

    def delete_back(self):
        if not self.head:
            print("List is empty")
            return
        if not self.head.next:
            self.head=None
            return
        last=self.head
        while last.next.next:
            last=last.next
        last.next=None
    def delete_front(self):
        if not self.head:
            print("The list is empty")
            return
        self.head=self.head.next
    def delete_pos(self,pos):
        if pos<0:
            print("invalid position")
            return
        if not self.head:
            print("List is empty!")
            return
        if pos==0:
            self.head=self.head.next
        current=self.head
        for _ in range(pos-1):
            if not current:
                print("Position out of bound")
                return
            current=current.next
        if not current.next:
            print("Position is out of bound")
            return
        current.next=current.next.next

    def search(self,key):
        check=self.head
        count=0
        while check:
            if check.data==key:
                print(f"Element found at index {count}")
                return
            count+=1
            check=check.next
        print("Element not found ")
    def printlist(self):
        last=self.head
        while last:
            print(last.data,end="->")
            last=last.next
        print("None")

def main():
    LL=Linkedlist()

    while True:
        print("/n***Menu***")
        print("Press 1 to insert node at back")
        print("Press 2 to insert node at front")
        print("Press 3 to insert node at any position")
        print("Press 4 to delete node at back")
        print("Press 5 to delete node at front")
        print("Press 6 to delete node at any position")
        print("Press 7 to search for an element in the linked list")
        print("Press 8 to display the current linked list")
        print("Press 9 to exit the program")

        choice=int(input("Enter your choice: "))

        if choice==1:
            data=int(input("Enter the data to be inserted at the back:"))
            LL.insert_back(data)

        elif choice==2:
            data=int(input("Enter the data to be inserted at the front:"))
            LL.insert_front(data)
        elif choice==3:
            data=int(input("Enter the data to be inserted at the position:"))
            pos=int(input("Enter the position where the data is to be inserted: "))
            LL.insert_pos(data,pos)
        elif choice==4:
            LL.delete_back()
        elif choice==5:
            LL.delete_front()
        elif choice==6:
            pos=int(input("Enter the position to be deleted : "))
            LL.delete_pos(pos)
        elif choice==7:
            key=int(input("Enter the item to be searched : "))
            LL.search(key)
        elif choice==8:
            LL.printlist()
        elif choice==9:
            print("The program is terminated, Thank you")
            break
        else:
            print("\n\nInvalid choice\n\n")
if __name__=='__main__':
    main()

    
