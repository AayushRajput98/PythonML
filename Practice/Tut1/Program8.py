def check(c):
    if(c.__len__()>1):
        raise Exception("The entered character is a string")
    else:
        if(c is 'a' or c is 'e' or c is 'i' or c is 'o' or c is 'u'):
            return True
        else:
            return False

c=input("Enter the character")

try:
    print(check(c))
except Exception as e:
    print(e)