
#list comprehension in python

fruits = ["phani", "banana", "choco", "kiran", "mahesh"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


#list comprehesnion method will reduce the syntax and it will seen in shorter form

fruits = ["phani", "banana", "choco", "kiran", "mahesh"]

newlist = [x for x in fruits if "a" in x]

print(newlist)


#conditonal execution in list comprehension

fruits = ["phani", "banana", "choco", "kiran", "mahesh"]

newlist = [x for x in fruits if x != "banana"]

print(newlist)


#expression

#to make all the input values upper case


fruits = ["phani", "banana", "choco", "kiran", "mahesh"]
newlist = [x.upper() for x in fruits]

print(newlist)


#to make all the input values lowerr case

fruits = ["pHhani", "bFFanana", "cFWFFSDFhoco", "kirDFDSFan", "mahFDDFesh"]
newlist = [x.lower() for x in fruits]

print(newlist)
