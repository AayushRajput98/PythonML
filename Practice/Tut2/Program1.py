import functools
def max_in_list(l):
    return functools.reduce(lambda x,y:x if x>y else y,l)
l=[1,2,3,4,5,12,16,23,30,13]
print(max_in_list(l))