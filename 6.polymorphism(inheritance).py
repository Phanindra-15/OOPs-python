class bird:
     def intro(self):
       print("There are many types of birds")
 
     def flight(self):
       print("Many of the birds can fly but some cannot fly ")
 
class parrot(bird):
     def flight(self):
       print("Parrots can fly")
 
class penguin(bird):
     def flight(self):
       print("Penguins do not fly")
 
obj_bird = bird()
obj_parr = parrot()
obj_peng = penguin()
 
obj_bird.intro()
obj_bird.flight()
 
obj_parr.intro()
obj_parr.flight()
 
obj_peng.intro()
obj_peng.flight()
