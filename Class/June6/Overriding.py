class one:
    def show(self):
        print("helloo!!")
class two(one):
    def show(self): #Overrides the above method
        super().show()
        print("BYe")

k=two()
k.show()