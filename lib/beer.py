

class Beer:
	def __init__(self, abv=None, ibu=None, name=None, desc=None):
		self.abv=self.sanitize(abv)
		self.ibu=self.sanitize(ibu)
		self.name=self.sanitize(name)
		self.desc=self.sanitize(desc)

	def sanitize(self, value):
		return value.encode('ascii','ignore').strip()

