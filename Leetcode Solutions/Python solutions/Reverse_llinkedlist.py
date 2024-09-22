class Node :
    def __init__(self,data):
        self.data=data
        self.next=None
n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
head=n1

n1.next=n2
n2.next=n3
n3.next=n4
n4.next=None

curr=head

while curr:
    print(curr.data,end='->')
    curr=curr.next
print('The Reveresed linked list is : ',end='')
prev,curr=None,head

while curr:
    temp=curr.next
    curr.next=prev
    prev=curr
    curr=temp

nhead=prev
while nhead:
    print(nhead.data,end='->')
    nhead=nhead.next