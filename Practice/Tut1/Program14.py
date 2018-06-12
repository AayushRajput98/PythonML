def overlapping(l1,l2):
    for i in l1:
        for j in l2:
            if str(i)==str(j):
                return True
    else:
        return False
l1=[1,2,3,"two",9.8,8,10,True]
l2=[1,2,4,6,"two",9.8]
print(overlapping(l1,l2))