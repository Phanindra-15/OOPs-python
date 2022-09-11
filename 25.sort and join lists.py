#to copy lists in python


thislist = ["phani","sumanth","hemanth","yuvan"]

mylist = thislist.copy()
print(mylist)

#2nd method using list

thislist = ["phani","sumanth","hemanth","yuvan"]
mylist = list(thislist)
print(mylist)

#joining of lists in python



list1 = ["aA", "Bb", "Cc"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

#2nd method csn be done by using append method

list1 = ["aA", "Bb", "Cc"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

#3rd method by using extend method to join lists
list1 = ["aA", "Bb", "Cc"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
