size=int(input("Enter the size of the array:"))
array=[]

for i in range(size):
    array.append(int(input("Enter the number:")))

target=int(input("Enter the target:"))

for i in range(size):
    for j in range(i+1,size):
        if array[i]+array[j]==target:
            print(i,j)
