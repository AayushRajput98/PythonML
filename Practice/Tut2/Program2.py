d={"One":"one","Two":"two","Three":"four","Four":"six","Five":"nine","Six":"three","Seven":"eight","Eight":"eleven"}
l=list(d.keys())
l.sort()
print(l)
print()
print("{ ",end="")
for i in l:
    print(i+":"+d[i],end=", ")
print("}")
l1=list(d.values())
print()
l1.sort()
print(l1)
print()
print("{ ",end="")
for j in l1:
    for i in list(d.keys()):
        if d[i] == j:
            print(i+":"+j,end=", ")
print("}")

