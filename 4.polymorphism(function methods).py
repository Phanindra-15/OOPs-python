class banana():

    
     def type(self): 
       print("vegetable")
       
     def color(self):
       print("orange")
       
class apple(): 
     def type(self): 
       print("fruit") 
     def color(self): 
       print("grey") 
     
def func(obj): 
       obj.type() 
       obj.color()
       
obj_banana = banana()

obj_apple = apple() 
func(obj_banana) 
func(obj_apple)
