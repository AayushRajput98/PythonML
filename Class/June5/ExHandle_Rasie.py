def sum(x):
    if (x>2000):
        raise Exception("You cant enter value greater than 2000")
    else:
        print("Success")
try:
    x=int(input("Enter the amount"))
    sum(x)
except Exception as e:
    print(e)