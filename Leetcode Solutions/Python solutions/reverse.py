def reverse(s):
    l=0
    r=len(s)-1
    while l<r:
        s[l],s[r]=s[r],s[l]
        l+=1
        r-=1
a=[]
n=int(input("Enter the size of the array:"))
for i in range(n):
    a.append(input("Enter the characters"))
reverse(a)
print(a)