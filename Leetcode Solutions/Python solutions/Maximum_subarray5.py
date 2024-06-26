def Max_subarray(array):
    max_sub=array[0]
    curr_sum=0
    for n in array:
        if curr_sum<0:
            curr_sum=0
        curr_sum+=n
        max_sub=max(max_sub,curr_sum)
    return max_sub
size=int(input("Enter the size of the array: "))
array=[]
for i in range(size):
    array.append(int(input(f"Enter the element {i+1}: ")))
print(Max_subarray(array))
