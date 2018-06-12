#Hybrid Inheritance

class one:
    def __init__(self):
        print("This is parent function")
class two(one):
    def __init__(self):
        super().__init__()
        print("This is child 1")
class three(one):
    def __init__(self):
        super().__init__()
        print("This is child 2")
obj1=three()
obj2=two()