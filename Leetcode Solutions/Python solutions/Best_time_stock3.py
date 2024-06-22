              
size=int(input('Enter the size of the array: '))
array=[]
for i in range(size):
    array.append(int(input(f'Enter the element {i+1} : ')))
min=array[0]
mp=0
for i in range(1,size):
    if array[i]<min:
        min=array[i]
        b=i+1
    elif array[i]-min>mp:
        mp=array[i]-min
        s=i+1
print('The maximum profit is : ',mp)
print(f'Stocks bought on day {b} and sold at day {s}')
        
            
