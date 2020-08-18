
class Move:

	def __init__(self):
		self.moveFrom = []
		self.moveTo = []
		self.makeMove = False

	def clear(self):
		self.moveFrom = []
		self.moveTo = []
		self.makeMove = False

	def addMove(self, move):

		if not self.moveFrom:
			self.moveFrom = move
		else:
			if self.moveFrom == move:
				self.clear()
			else:
				self.moveTo = move
				self.makeMove = True


