
import pygame as pg
from constants import TILE_SIZE

def handle_events(event):

	returnKey = {}

	if event.type == pg.QUIT:
		returnKey = {'quit': True}
	elif event.type == pg.MOUSEBUTTONDOWN:
		returnKey = handle_mouseEvent(pg.mouse)

	return returnKey

def handle_mouseEvent(mouse):

	coordinates = mouse.get_pos()
	x = coordinates[0] // TILE_SIZE
	y = coordinates[1] // TILE_SIZE

	returnKey = {'left_click': (x,y)}

	return returnKey


