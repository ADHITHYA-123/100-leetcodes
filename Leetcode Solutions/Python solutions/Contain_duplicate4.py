def contain_duplicate(array):
    seen=set()
    for element in array:
        if element in seen:
            return True
        else:
            seen.add(element)
size=int(input("Enter the size of the array :"))
array=[]
for i in range(size):
    array.append(int(input(f"Enter the {i+1} element : ")))
print(contain_duplicate(array))