#values in set are added to a heap index, thats why the set elements are not ordered and the index is provided to them at run-time
d={"Aayush","Deepak","Apaar","Durgesh","Aayush","xyz"} #it omits the duplicate value
e={"Aayush","Mansa","Sagar","Deepak"}
d.remove("xyz")  #Remove the element if present in the set otherwse raises error
print(d)
print()
d.discard("xyz") #Remove the element if exist
print(d)
print()
print(d.intersection(e))
print()
print(d.union(e))
print()
print(d.difference(e))
print()
e.add("Sargam")
print(e)
print()
f=e.copy()
print(f)
print()
print(f.issubset(e))
print()
print(f.issuperset(e))
print()
d.update("Names")
print(d)
print()
print(d.symmetric_difference(e)) #union-intersection
print()
a={1,2,3}
b={4,1,5}
print(a&b)  #ientesrection
print(a|b)  #union
print(a^b)  #symmetric_difference
print(a-b)  #difference