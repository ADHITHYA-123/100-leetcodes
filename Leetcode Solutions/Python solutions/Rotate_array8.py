size=int(input("Enter the size of the array:"))
array=[]
temp=0
for i in range(size):
    array.append(int(input("Enter the number:")))
k=int(input("Enter the number of rotations:"))
k=k%size
l,r=0,size-1
while l<r:
    array[l],array[r]=array[r],array[l]
    l+=1
    r-=1
l=0
r=k-1
while l<r:
    array[l],array[r]=array[r],array[l]
    l+=1
    r-=1
l,r=k,size-1
while l<r:
    array[l],array[r]=array[r],array[l]
    l+=1
    r-=1
print(array)