class Persons():
	"""docstring for Persons"""
	def __init__(self, name, job, pay = 0):
		self.name = name
		self.job = job
		self.pay = pay

	def __repr__(self):
		return(self.name, self.job, self.pay)
		
bob = Persons("Bob Smith", "dev")
print(bob)