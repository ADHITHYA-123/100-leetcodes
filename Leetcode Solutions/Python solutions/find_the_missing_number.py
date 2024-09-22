arr=[0,1,3]
n=3
sum_real=int(n*(n+1)/2)
sum=0
for i in arr:
    sum+=i
print("The missing number is "+str(sum_real-sum))