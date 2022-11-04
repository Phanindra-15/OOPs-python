#Accessing array elementd based on their index by importing array


#we can access array elements with this tchnique

import array as arr  
a = arr.array('i', [2, 4, 6, 8])  
print("first element of array:", a[0])  
print("second element of array:", a[1])  
print("last element of array:", a[-1])


#Array elements are mutuable and thus the elements can be changed

import array as arr  
numbers = arr.array('i', [1, 2, 3, 5, 7, 10])  
   
  
numbers[0] = 0     
print(numbers)    
   
  
numbers[2:5] = arr.array('i', [4, 6, 8])    
print(numbers)  
