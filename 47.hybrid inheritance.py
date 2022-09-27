class Parent:
     def func1(self):
         print("this is phanindra punati")
 
class Child(Parent):
     def func2(self):
         print("python is a object oriented programming language")
 
class Child1(Parent):
     def func3(self):
         print("python supports all types of inheritances"):
 
class Child3(Parent , Child1):
     def func4(self):
         print("python is a high level programminng language")
 
ob = Child3()
ob.func1()
