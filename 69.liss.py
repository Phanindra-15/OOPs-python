#Manipulating lists in python
'''total=0
count=0
while True:
    
    inp=input("enter a number")
     
    if inp =='done':
        break
    value=float(inp)
    total=total+ value
    count=count+1

avg=total/count
print('average:',avg)


#using list append method

numl=list()
while True:
    inp=input("enter a number  :")
    if inp == 'done':
        break
    value=float(inp)
    numl.append(value)
avg=sum(numl) / len(numl)
print("average",avg)'''

fruit = 'Banana'
fruit[0] = 'b'
print(fruit)
