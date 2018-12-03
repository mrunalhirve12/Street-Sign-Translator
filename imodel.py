from abc import ABCMeta, abstractmethod

class IModel():
	"""
	Abstract class to represent model
	"""
	__metaclass__ = ABCMeta
	
	@abstractmethod
	def list(self):
		"""
		Abstract method to return all rows in the database 
		"""
		pass

	@abstractmethod
	def insert(self):
		"""
		Astract method to insert one record to database
		"""
		pass
