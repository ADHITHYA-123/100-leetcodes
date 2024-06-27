size=int(input("Enter the size of the array: "))
array=[]
count=0
for i in range(size):
    array.append(int(input(f"Enter the element {i+1} :")))
for i in range(size):
    if array[i]==0:
        count+=1
for i in range(count):
    array.remove(0)
for i in range(count):
    array.append(0)
print(array)