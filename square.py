

class Square:

	def __init__(self, name):
		self.name = name
		self.number = ""
		self.occupant = None

	def isOccupied(self):
		if self.occupant:
			return True

	def getOccupant(self):
		return self.occupant
		

