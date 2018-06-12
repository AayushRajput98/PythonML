def max_of_three(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    elif b>c:
        return b
    else:
        return c

a=int(input("Enter the number"))
b=int(input("Enter the number"))
c=int(input("Enter the number"))
print("The maximum out of the three is ",max(a,b,c))