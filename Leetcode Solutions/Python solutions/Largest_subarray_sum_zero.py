arr = [15, -2, 2, -8, 1, 7, 10, 23]

d = {}
sum = 0
result = 0

for i in range(len(arr)):
    sum += arr[i]
    
    # If cumulative sum is 0, update result
    if sum == 0:
        result = i + 1
    
    # Check if sum has been seen before
    if sum in d:
        # Calculate the length of the subarray
        result = max(result, i - d[sum])
    else:
        # Store the sum with its index
        d[sum] = i

print(str(result) + " is the length of the largest subarray with sum equal to zero")
