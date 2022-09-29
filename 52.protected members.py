class Student:
    
    _schoolName = 'Sri chaitanya techno School' 

    def __init__(self, name, age):
        self._name=name 
        self._age=age

std = Student("phanindra", 25)
h=std._name
g=std._age
print(h)
print(g)
