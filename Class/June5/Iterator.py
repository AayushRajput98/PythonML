l=[1,2,3,4,5,6]
k=iter(l)
try:
    print(next(k))
    print(next(k))
    print(next(k))
    print(next(k))
    print(next(k))
    print(next(k))
    print(next(k))
    print(next(k))
except Exception as e:
    print(e)
