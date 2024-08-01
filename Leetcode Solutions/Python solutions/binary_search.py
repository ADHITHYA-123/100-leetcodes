arr=[1,2,3,4,5,6,7,8,9,10]

check=0
target=2
l=0
u=len(arr)-1

while l<=u:
    mid=(l+u)//2
    if arr[mid]==target:
        print("Item found in the array!")
        check+=1
        break
    elif arr[mid]<target:
        l=mid+1
    else:
        u=mid-1
if check==0:
    print("item not found")
