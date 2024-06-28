size=int(input("Enter the size of the array: "))
array=[]
for i in range(size):
    array.append(int(input(f"Enter the element {i+1} : ")))

seen=set()
l=1
for r in range(1,size):#we dont take zero as it can never be a duplicate value
    if array[r]!=array[r-1]:
        array[l]=array[r]
        l+=1
print(l)


