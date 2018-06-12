t=(1,2,3,9,8,7,4,12,16,9,10)
def sort(t):
    l=list(t)
    l.sort()
    for i in l:
        print(i, end=" ")
sort(t)