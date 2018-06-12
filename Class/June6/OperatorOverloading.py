class one:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def __add__(self, other):
        return one(self.a+other.a,self.b+other.b)
    def __str__(self):
        return ("({0},{1})".format(self.a,self.b))
k=one(2,4)
k1=one(4,5)
k3=k+k1
print(k3)