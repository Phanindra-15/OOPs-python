#python simple program to explain init


class Student:  
    def __init__(self, st_name, st_class, st_marks):  
        self.st_name = st_name  
        self.st_class = st_class  
        self.st_marks = 67  
S1 = Student("phanindra", 10, 97)  
print(S1.st_name)  
print(S1.st_class)
print(S1.st_marks)
