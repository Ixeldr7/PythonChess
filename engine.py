
from board import Board
import itertools
import pygame as pg

WIDTH = 512
HEIGHT = 512
DIMENSION = 8
TILE_SIZE = HEIGHT / DIMENSION
MAX_FPS = 15

def main():
	xAxis = ['A','B','C','D','E','F','G','H']
	yAxis = ['1','2','3','4','5','6','7','8']

	pg.init()
	BLACK = ((200,190,140))
	WHITE = pg.Color('white')
	colours = itertools.cycle((WHITE,BLACK))

	screen = pg.display.set_mode((WIDTH, HEIGHT))
	screen.fill(WHITE)
	clock = pg.time.Clock()
	board = Board(xAxis, yAxis)
	
	running = True
	while running:
		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False

		renderGameState(screen, board, colours, xAxis, yAxis)
		clock.tick(MAX_FPS)
		pg.display.flip()

def renderGameState(screen, board, colours, xAxis, yAxis):
	renderBoard(screen, board, colours)
	renderPieces(screen, board, xAxis, yAxis)

def renderBoard(screen, board, colours):

	for y in range(DIMENSION):
		for x in range(DIMENSION):
			rect = (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
			pg.draw.rect(screen, next(colours), rect)
		next(colours)

	return 0

def getPiece(board, currentSquare):
	for square in board.squares:
		if square.name == currentSquare:
			piece = isOccupied(board, square)
			if piece:
				print(piece.name)
				print(str(piece.image))
				break

	return piece

def isOccupied(board, square):
	for piece in board.pieces:
		if square.occupant == piece:
			return piece

def renderPieces(screen, board, xAxis, yAxis):

	for y in range(DIMENSION):
		for x in range(DIMENSION):
			currentSquare = str(xAxis[x]) + str(yAxis[y])
			piece = getPiece(board, currentSquare)
			if piece:
				screen.blit(piece.image, pg.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

	return

if __name__ == '__main__':
	main()