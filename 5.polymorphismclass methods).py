class India():
    
     def capital(self):
       print("New Delhi")
 
     def sport(self):
       print("cricket")
 
class USA():
     def capital(self):
       print("Washington")
 
     def sport(self):
       print("basket ball")
 
obj_ind = India()

obj_usa = USA()

for country in (obj_ind, obj_usa):
    country.capital()
    country.sport()
