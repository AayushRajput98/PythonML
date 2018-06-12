class one:
    def add(self):
        print("Add function")
    def add(self,a,b):  #This method overrides the previous method on account of dynamic allocation
        print(a+b)
k=one()
k.add(2,3)