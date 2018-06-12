class data:
    __count=0    #Private data member
    def one(self):
        self.__count+=1
        print(self.__count)
k=data()
k.one()
k.one()
#print(k.__count) Private member cant be accessed outside of the class
print(k._data__count)