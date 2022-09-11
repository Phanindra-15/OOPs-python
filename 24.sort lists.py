#sorting lists in python

#lists can be sorted in different ways

#alphanumerically

thislist = ["phani", "man", "kiran", "pinky", "basket"]
thislist.sort()

print(thislist)


#sort descending
thislist = ["phani", "man", "kiran", "pinky", "basket"]

thislist.sort(reverse = True)

print(thislist)


#case insensitive sort

thislist = ["Phani", "man", "Kiran", "pinky", "Basket"]
thislist.sort()

print(thislist)


#reverse order
thislist = ["phani", "man", "kiran", "pinky", "basket"]
thislist.reverse()
print(thislist)
