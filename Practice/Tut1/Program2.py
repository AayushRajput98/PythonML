def print_number(x):
    if x < 0:
        raise Exception("The Number should be greater than 0")
    else:
        while x >= 0:
            print(x, end=" ")
            x = x - 1


try:
    x=int(input("Enter the number"))
    print_number(x)
except Exception as e:
    print(e)
