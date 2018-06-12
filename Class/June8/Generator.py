def my_gen():
    n=1
    print("This is printed first")
    yield n                           #Creates an iterator that halts at every yield and returns a value
    n+=1
    print("This is printed second")
    yield n
    n+=1
    print("This is printed third")
    yield n
a=my_gen()
print(next(a))
print(next(a))
print(next(a))