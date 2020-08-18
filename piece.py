

class Piece:

	def __init__(self, type, colour, name, squareName):
		self.name = name
		self.colour = colour
		self.type = type
		self.image = ""
		self.squareName = squareName
		self.square = ""
		self.captured = False
