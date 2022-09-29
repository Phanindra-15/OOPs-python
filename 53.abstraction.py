from abc import ABC  
  
class Polygon(ABC):      
   def sides(self):   
      pass  
  
class Triangle(Polygon):   
  
     
   def sides(self):   
      print("triangle has 3 sides")   
  
class Pentagon(Polygon):   
  
     
   def sides(self):   
      print("pentagon has 5 sides")   
  
class Hexagon(Polygon):   
  
   def sides(self):   
      print("Hexagon has 6 sides")   
  
class square(Polygon):   
  
   def sides(self):   
      print("I have 4 sides")   
  

t = Triangle()   
t.sides()   
  
s = square()   
s.sides()   
  
p = Pentagon()   
p.sides()   
  
K = Hexagon()   
K.sides()   
