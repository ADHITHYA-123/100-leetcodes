# def atoi(s):
#     sum=0
#     sign=1
#     l=0
#     if s[0]=='-':
#         sign=-1
#         s=s[1:]
        
#     for i in range(len(s)):
#         if s[i]=='0':
#             sum=sum*10
#         elif s[i]=='1':
#             sum=sum*10+1
#         elif s[i]=='2':
#             sum=sum*10+2
#         elif s[i]=='3':
#             sum=sum*10+3
#         elif s[i]=='4':
#             sum=sum*10+4
#         elif s[i]=='5':
#             sum=sum*10+5
#         elif s[i]=='6':
#             sum=sum*10+6
#         elif s[i]=='7':
#             sum=sum*10+7
#         elif s[i]=='8':
#             sum=sum*10+8
#         elif s[i]=='9':
#             sum=sum*10+9
           
#         else:
#             return -1
#     return sign*sum

def atoi(s):
    dig_map={
        '0':0,
        '1':1,
        '2':2,
        '3':3,
        '4':4,
        '5':5,
        '6':6,
        '7':7,
        '8':8,
        '9':9,
    }
    sum=0
    sign=1
    if s[0]=='-':
        sign=-1
        s=s[1:]
    for i in s:
        if s not in dig_map:
            return -1
        sum=sum*10+dig_map[i]
    return sign*sum

def main():
    str=input("Enter the string: ")
    print(atoi(str))

if __name__=='__main__':
    main()