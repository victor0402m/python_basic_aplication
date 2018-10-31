import uuid

class ClientModel:
	"""docstring for Clients"""
	def __init__(self, name, age, company, job, uid=None):
		self.name = name
		self.age = age
		self.company = company
		self.job = job
		self.uid = uid or uuid.uuid4()

	def to_dic(self):
		return vars(self)

	@staticmethod
	def shema():
		return ['name', 'age', 'company', 'job', 'uid']
		