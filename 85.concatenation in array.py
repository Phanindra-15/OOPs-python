
# Array concatenation
import array as arr

a=arr.array('d',[1.11 , 12.1 ,3.11,2.6,71.8])  
b=arr.array('d',[3.7,8.6])  
c=arr.array('d')  
c=a+b  
print("Array c = ",c)



#To delete elements from array

import array as arr

number = arr.array('i', [1, 2, 3, 3, 4,5,6])

del number[2]
del number[4]
print(number)
