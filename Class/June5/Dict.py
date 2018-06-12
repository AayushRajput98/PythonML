d={"id":101,"name":"Aayush","lastname":"Rajput","Salary":"100000"}
print(d.setdefault("Contact",9675810661))
for i in d.items():
    print(i)
print("")
print(d.items())
print("")
print(d.pop("Salary"))
print("")
print(d.popitem())
d["hello"]=10101
print(d)
