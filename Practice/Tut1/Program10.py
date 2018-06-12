import functools
def sum(l):
    return functools.reduce(lambda x,y:x+y,l)
def mul(l):
    return functools.reduce(lambda x,y:x*y,l)
l=[1,2,3,4]
print(sum(l))
print(mul(l))

