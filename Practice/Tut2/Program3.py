d={"One":"one","Two":"two","Three":"four","Four":"six","Five":"nine","Six":"three","Seven":"eight","Eight":"eleven"}
l1=list(d.keys())
l2=list(d.values())
len=d.__len__()
d.clear()
for i in range(0,len):
    d.setdefault(l2[i],l1[i])
print(d)