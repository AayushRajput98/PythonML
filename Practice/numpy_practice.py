import numpy as np
a=np.array([1,2,3,4,5,'aayush'])
print(a.itemsize)
a=np.array(['aaysuh'])
print(a.itemsize)
s=[1,2,3,4]
a=np.fromiter(s,dtype='i1')
print(a)
a=np.arange(12).reshape(4,3)
row=np.array([(0,0),(3,3)])
col=np.array([(0,2),(0,2)])
y=a[row,col]
print(a.T)  #Transpose of the array
print(y)
# a=np.array([1,2,3,np.nan])
# print(a[~np.isnan(a)])
for i in np.nditer(a, op_flags=['readwrite']):
    a[...]=2*a
print(a)
print(a.flatten(order='C'))
x=np.array([(1,),(2,),(3,)])
y=np.array([4,5,6])
# b=np.broadcast_arrays(x,y)
# for i in np.nditer(b):
#     print(i)
print(x)
print("sum",x+y)

print()

x=np.arange(1,5).reshape(2,2)
print(x)
print()
y=np.arange(5,9).reshape(2,2)
print(y)
print()
x1=np.concatenate((x,y), axis=0)
print(x1)
print()
x2=np.stack((x,y))
print(x2)
a=np.arange(1,7).reshape(2,3)
print()
print(a)
print()
b=np.append(a,[7,8,9])
print(b)
print()
c=np.append(a,[(7,1,2),(4,3,4)],axis=1)
print(c)
a=np.array([1,2,3])
b=np.array([(9,4,5,6),(8,5,6,7)])
print(np.sort(b,axis=0,kind='quicksort'))