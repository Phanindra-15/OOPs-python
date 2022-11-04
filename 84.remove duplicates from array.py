# removing duplicates  from arrray in python


array=[1,2,3,1,2,3,4,5,4,4]

l=[]

for i in array:
    if i not in l:
        l.append(i)
    
print(l)


#removing duplicates from a string

s=[12,1,1,12,12,1,3,3,4]
m=[]
for i in s:
    if i not in m:
        m.append(i)
print(m)
