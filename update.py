from globals import *
from setup import *
from segment import * 
global dy
global dx 

dy = 0
dx = 0

def snakeUpdate():
	global dy
	global dx
	canvas.fill(WHITE)

	for event in pygame.event.get():	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				dx = 0
				dy = 0.33
			elif event.key == pygame.K_UP:
				dx = 0
				dy = -0.33
			elif event.key == pygame.K_LEFT:
				dy = 0
				dx = -0.33
			elif event.key == pygame.K_RIGHT:
				dy = 0
				dx = 0.33

	for segment in snakeSegmentLocations:
		segment.posx += dx
		segment.posy += dy

		pygame.draw.rect(canvas, BLACK, (segment.posx, segment.posy, segment.size, segment.size))

	