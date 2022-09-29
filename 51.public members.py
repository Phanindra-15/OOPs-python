class Student:
    schoolName = 'Sri chaitanya techno School' 

    def __init__(self, name, age):
        self.name=name 
        self.age=age

std = Student("Steve", 25)
h=std.schoolName
g=std.age
print(h)
print(g)
