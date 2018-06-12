import functools
def sum():
    x=12
    y=14
    print(x+y)

'''Override'''
def sum(x,y):  #overrides the previous sum
    print(x+y)
def subtract():
    x=14
    y=5
    print(x-y)
#sum()
sum(12,20)
subtract()
#value passed is called is called argument and the variables in the body is called parameters
def sum(x,y,z):
    return x+y*z
print(sum(2,5,12))

'''optional parameters'''
def show(x,y,z=90):
    print(x,y,z)
show(1,2)
show(1,2,3)
'''named parameters'''
show(z=9,x=8,y=3) #named parameters

'''Lambda expression'''
#lamda expression: anonymus function, in-line function, security-purpose, reduce complexity
add=lambda x,y:x*y
print(add(10,2))
print()
print()

#functions that support the use of lambda expression

'''Map function'''
Celsius=[39.2, 36.5, 37.3, 37.8]
Fahrenheit=map(lambda x:(float(9)/5)*x+32, Celsius)
for i in Fahrenheit:
    print(i)

print()

'''Filter Function'''
fib=[0,1,1,2,3,4,8,13,21,34,55]
result=filter(lambda x:x%2, fib)
for i in result:
    print(i)

'''Reduce Function'''
mylist=[102,2,3,123,345]
print(functools.reduce(lambda x,y: x if(x>y) else y,mylist))

mylist=[102,2,3,123,345]
print(functools.reduce(lambda x,y: x+y,mylist))

'''Map function operates on list element individually. It can support more than one argument.
   Filter function operates on list element such that to filter out some of the element and to change the elements.
   Reduce function is used to compare the elements of a list and return one reduced output'''