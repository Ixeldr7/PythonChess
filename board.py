from square import Square
from piece import Piece
import itertools
import pygame as pg

WHITE = "WHITE"
BLACK = "BLACK"
SQUARES = 64

class Board:

	def __init__(self, xAxis, yAxis):
		self.xAxis = xAxis
		self.yAxis = yAxis
		self.width = len(xAxis)
		self.height = len(yAxis)
		self.squares = self.initialise_squares()
		self.pieces = self.initialise_pieces()

	def initialise_squares(self):

		squareNames = []
		for y in range(self.height):
			for x in range(self.width):
				squareNames.append(str(self.xAxis[x]) + str(self.yAxis[y]))

		squares = [Square(str(squareNames[s])) for s in range(SQUARES)]

		return squares

	def initialise_pieces(self):

		colours = itertools.cycle((WHITE, BLACK))
		pawnNames = itertools.cycle(("wp","bp"))
		rookNames = itertools.cycle(("wR","bR"))
		knightNames = itertools.cycle(("wN","bN"))
		bishopNames = itertools.cycle(("wB","bB"))
		queenNames = itertools.cycle(("wQ","bQ"))
		kingNames = itertools.cycle(("wK","bK"))

		pawnStarts = ["A2", "A7", "B2", "B7", "C2", "C7", "D2", "D7", 
					"E2", "E7", "F2", "F7", "G2", "G7", "H2", "H7"]
		rookStarts = ["A1", "A8", "H1", "H8"]
		knightStarts = ["B1", "B8", "G1", "G8"]
		bishopStarts = ["C1", "C8", "F1", "F8"]
		queenStarts = ["D1", "D8"]
		kingStarts = ["E1", "E8"]

		pawns = [Piece("PAWN", next(colours), next(pawnNames), pawnStarts[x]) for x in range(0, 16)]
		rooks = [Piece("ROOK", next(colours), next(rookNames), rookStarts[x]) for x in range(0, 4)]
		knights = [Piece("KNIGHT", next(colours), next(knightNames), knightStarts[x]) for x in range(0, 4)]
		bishops = [Piece("BISHOP", next(colours), next(bishopNames), bishopStarts[x]) for x in range(0, 4)]
		queens = [Piece("QUEEN", next(colours), next(queenNames), queenStarts[x]) for x in range(0, 2)]
		kings = [Piece("KING", next(colours), next(kingNames), kingStarts[x]) for x in range(0, 2)]

		pieces = pawns + rooks + knights + bishops + queens + kings

		loadImages(pieces)

		for square in self.squares:
			for piece in pieces:
				if square.name == piece.squareName:
					piece.square = square
					square.occupant = piece

		#print(pieces[1].square)
		#print(pieces[1].square.name)
		#print(pieces[1].squareName)

		return pieces

	def setup_pieces(self):

		return 0

	def defaultBoardState(self):
		
		return 0

def loadImages(pieces):
	for piece in pieces:
		piece.image = pg.image.load("images/" + piece.name + ".png")