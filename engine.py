from constants import WIDTH, HEIGHT, DIMENSION, TILE_SIZE, MAX_FPS
from board import Board
import itertools
import pygame as pg
from input_handlers import handle_events
from move import Move

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

	move = Move()

	running = True
	while running:
		for event in pg.event.get():
			action = handle_events(event)
			
			if action:
				quit = action.get('quit')
				left_click = action.get('left_click')
			else:
				quit = None
				left_click = None

			if quit:
				running = False

			if left_click:
				x,y = left_click
				selectedSquare = str(board.xAxis[x]) + str(board.yAxis[y])
				move.addMove(selectedSquare)
				
				if move.makeMove:
					board.makeMove(move)
					move.clear()

		renderGameState(screen, board, colours)
		clock.tick(MAX_FPS)
		pg.display.flip()

def renderGameState(screen, board, colours):
	renderBoard(screen, board, colours)
	renderPieces(screen, board)

def renderBoard(screen, board, colours):

	for y in range(DIMENSION):
		for x in range(DIMENSION):
			rect = (x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE)
			pg.draw.rect(screen, next(colours), rect)
		next(colours)

	return 0

def renderPieces(screen, board):

	for y in range(DIMENSION):
		for x in range(DIMENSION):
			currentSquare = str(board.xAxis[x]) + str(board.yAxis[y])
			piece = board.getPiece(currentSquare)
			if piece and piece.captured == False:
				screen.blit(piece.image, pg.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

	return

if __name__ == '__main__':
	main()