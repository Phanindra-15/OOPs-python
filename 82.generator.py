
def GeneratorFun():
	yield 1		
	yield 2		
	yield 3
	yield 4


for value in GeneratorFun():
	print(value)

#generator object


def GeneratorFun():
	yield 1
	yield 2
	yield 3


x =GeneratorFun()


print(next(x))
print(next(x))
print(next(x))
