size=int(input("Enter the size of the array:"))
array=[]
temp=0
for i in range(size):
    array.append(int(input("Enter the number:")))
res=0
for i in array:
    res=res^i
print(res)