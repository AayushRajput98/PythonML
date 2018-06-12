class a:
    def __init__(self):
        print("Parent constructor called")

class b(a):
    __secret=0
    def __init__(self,x=0, y=0, z=0):
        print("Child Constructor is called")
        self.x=x
        self.y=y
        self.z=z
        self.__secret+=1
    def methods(self):
        print("Child method is called")
        print(self.x,self.y,self.z)
obj=b(12,13,14)
obj1=b()
obj2=b()
obj.methods()
print(obj._b__secret)
print(obj1._b__secret)
print(obj2._b__secret)


