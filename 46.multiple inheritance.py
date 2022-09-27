class Parent:
   def func1(self):
       
        print("my name is venkata phanindra kumar")
class Parent2:
    
   def func2(self):
        print("my name is yuvan mandadi")
class Child(Parent , Parent2):
    
    def func3(self):
        print("my name is jeevan mundadi")
 
ob = Child()

ob.func1()
ob.func2()
ob.func3()
