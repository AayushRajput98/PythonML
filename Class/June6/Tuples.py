#Tuples are useful to store a collection of value that cant be modified, used for security.
#Denoted by paranthesis

t= 1,2,3,4,5,6,7,8,9,0    #Static memory allocation
print(t)
print(t[8])
p=9,   #To store a single value in the tuple
print(p)
print(t[1:5])
print(t[::-1])
for i in t:
    print(i,end=" ")
print()
tuple={1,2,3},1,2,3,4
print(tuple)
for i in tuple[0]:
    print(i)
t=1,2,3,4,5
t1=6,7,8,9,10
t3=t+t1#We have to regularly change the reference because same variable cant be updated
print(t3)

x=int(input("Enter the number"))
if x in t3:
    print(str(x)+" is successfully found in the tuple and is present "+str(t3.count(x))+" times")
print(max(t))
print(min(t))
print(sum(t))

del t
#print(t)  Tuple is deleted and hence not defined