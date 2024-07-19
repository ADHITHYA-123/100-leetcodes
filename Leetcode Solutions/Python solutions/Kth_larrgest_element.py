
def quickselect(arr,k,l,r):
    pivot,p=arr[r],l
    for i in range(l,r):
        if arr[i]<=pivot:
            arr[i],arr[p]=arr[p],arr[i]
            p+=1
    arr[p],arr[r]=arr[r],arr[p]
    if p>k:
        quickselect(arr,k,l,p-1)
    elif p<k:
        quickselect(arr,k,p+1,r)
    else:
        print(f"The kth largest element is : {arr[p]}")
    
size=int(input('Enter the size of the array: '))
arr=[]
for i in range(size):
    arr.append(int(input(f'Enter the element {i+1} : ')))
k=int(input('Enter the value of k: '))
k=size-k
quickselect(arr,k,0,size-1)