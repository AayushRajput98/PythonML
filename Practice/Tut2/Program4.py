import random, functools
d={}
for i in range (0,20):
    d.setdefault(i,random.randrange(1,100))
print(d)
l=list(d.values())
print(l)
result=filter(lambda x:x if l.count(x)>=2 else None,l)
for i in result:
    print(i,end=" ")
if result == None:
    print("Duplicates doesnot EXIST")
else:
    print("Duplicates EXIST")
