def is_member(x,a):
    for i in a:
        if str(i)==x:
            return True
    return False
a=[1,2,3,"one",True,9,9.8,7.8,[1,2,3]]
x=input("Enter the element to be checked")
print(is_member(x,a))