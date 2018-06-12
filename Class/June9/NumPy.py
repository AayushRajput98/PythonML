import numpy as np, pandas as pd, time, sys
a=np.array([1,2,3,4,5,6,7])
print(a)
b=np.array([(1,2,3),(4,5,6)])
print(b)
print("Dimenssions of array b",b.shape)
s=range(100)
print(sys.getsizeof(15)*len(s))
print(a.ndim, b.ndim)
print(b.sum(axis=0),b.sum(axis=1)) #axis=0 means sum of coloumns and axis=1 means sum of rows
print(np.ravel(b, order='A'))  #Row after row
print(np.ravel(b, order='F'))  #Coloumn after coloumn
print(np.std(a))  #To calculate standard deviation
print(np.mean(b))
print(b.reshape(3,2)) #To reshape a 2D array, change the number of columns
print(np.array([1,2,"Aayush"])) #converts all the other to string datatype
print(b[0:2,2])
print("Reversing row order:",b[::-1])  #starting row : dest row : step
print("Reversing every element in row: ",b[::-1,::-1]) #reversing the rows as well as coloumn
print("Sum = ",[1,2,3]+b)
print(b.itemsize)
a=np.arange(10).reshape(2,5)
print(a)
a1=np.arange(15).reshape(3,5)
a2=[4,5,6]
vs=np.vsplit(a1,3) #splits the rows
print(vs[0],vs[1])
hs=np.hsplit(a1,5) #splits the coloumns
for i in np.nditer(a1, order='C'):
    print(i, end=" ")
print()
for i in np.nditer(a1, order='F', flags=['external_loop']):
    print(i)
b=np.arange(3,15,4).reshape(3,1)
print(b)
for x,y in np.nditer([a1,b]):
    print(x,y)
a=np.array([(1,5),(2,9),(3,7)])
print(a)
print((np.ptp(a)))
print(np.nonzero(a))
b=a.view()
print(b)
b[0,1]=10
print(b)
print(b.reshape(2,3))
print(a)
print()
print()
print()
b=a.copy()
print(b)
print()
b[0,1]=11
print(b)
print()
print(b.reshape(2,3))
print()
print(a)
print()
print()
print()
