class Persons():
	"""docstring for Persons"""
	def __init__(self, name, job, pay = 0):
		self.name = name
		self.job = job
		self.pay = pay

	def lastName(self):
		return self.name.split()[-1]

	def giveRaise(self, percent):
		self.pay = int(self.pay * (1+percent))
		return self.pay

	def __repr__(self):
		return '[Person:  %s, %s]' % (self.name, self.pay)

class Manager(Persons):
	"""docstring for ClassName"""
	def giveRaise(self, percent, bonus):
		Persons.giveRaise(self, percent + bonus)
		
if __name__ == '__main__':

	bob = Persons("Bob Smith", "dev")
	sue = Persons("Sue Jone", "dev", 100000)
	print(bob)
	print(sue)
	print bob.lastName(), sue.lastName()
	print("Pay ==>" , sue.giveRaise(0.1))
	tom = Manager('Tom Luke', 'mgr', 100000)
	tom.giveRaise(.1,.1)
	print(tom.pay)
	
