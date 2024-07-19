n=int(input("Enter the size of fibonacci sequence to be printed: "))
arr=[0]*n
print(arr)
arr[0],arr[1]=1,1
for i in range(2,n):
    arr[i]=arr[i-1]+arr[i-2]
print(arr)