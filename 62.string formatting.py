price = 49
txt = "The price is {} rupees"
print(txt.format(price))

#we can add multiple values to it

q = 3
i = 567
p = 49
myorder = "I want {} pieces of item number {} for {:.2f} dollars."
print(myorder.format(q, i, p))



#string formmatting based on index numbers

q = 3
i = 567
p = 49
myorder = "I want {0} pieces of item number {1} for {2:.2f} dollars."
print(myorder.format(q, i, p))


#

age = 21
name = "Phani"
grade= "A"
txt = "His name is {1}. {1} is {0} years old.{1} is a {2} grade student"
print(txt.format(age, name,grade))
