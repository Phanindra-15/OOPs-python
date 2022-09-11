#lmabda expression in python

#it means that an expresssion that can take any number of arguments byt return only one expression is called as lambda expressuion



x = lambda a : a + 10
y = lambda a : a * 10
z = lambda a : a ** 10
print(x(5))
print(y(5))
print(z(5))


#it can be applicabl for multiple number of arguments also

x = lambda a, b : a + b
y = lambda a, b : a * b

z = lambda a, b : a ** b
print(x(5, 6))
print(y(25, 60))
print(z(15, 6))

x = lambda a, b, c : a + b + c
print(x(51, 61, 32))
