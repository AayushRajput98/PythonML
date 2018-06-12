def len(s):
    counter=0
    for i in s:
        counter=counter+1
    return counter
s=input("Enter the string")
print("The length of the string is ",len(s))