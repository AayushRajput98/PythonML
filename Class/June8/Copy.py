import copy
l=[[1,2,3,4],[5,6,7,8],[9,7,6,5]]

#Deep Copy

xs=copy.deepcopy(l)
print(xs)

#Shallow Copy

xl=copy.copy(l)
print(xl)

#If elements are changed in l then it will be reflected in xl as xl stores the refrence of the list

l[1][1]=0
print(xs) #deep copy: Copies the structure and creates an independent object
print(xl) #shallow copy: just copies the reference of the list object

