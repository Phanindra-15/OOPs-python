
#python even support multilevel inheritance


class mother:
 
	def __init__(self, mothername):
		self.mothername = mothername
 

class father(mother):
	def __init__(self, mothername, fathername):
		self.fathername = fathername
		mother.__init__(self, mothername)
 

class son(father):
	def __init__(self,sonname, mothername, grandmaname):
		self.sonname = sonname
		father.__init__(self, mothername, fathername)
 
	def print_name(self):
		print('mother name :', self.mothername)
		print("father name :", self.fathername)
		print("Son name :", self.sonname)
