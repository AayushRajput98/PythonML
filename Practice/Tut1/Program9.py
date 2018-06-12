from Practice.Tut1.Program8 import check
s=input("Enter the string")
s1=""
for i in s:
    if check(i) or i=="":
        s1=s1+i
    else:
        s1=s1+i+"o"+i
print(s1)