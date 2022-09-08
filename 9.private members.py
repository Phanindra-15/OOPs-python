class Base:
	def __init__(self):
		self.a = "phanindra punati"
		self.__c = "GeeksforGeeks"


class Derived(Base):
	def __init__(self):
		Base.__init__(self)
		print("Calling private member of base class: ")
		print(self.a)



obj1 = Base()
obj2=Derived()

print(obj1.a)
