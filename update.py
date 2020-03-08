from globals import *
from setup import *
from segment import * 
# from apple import *

global dy
global dx 
import math

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
				dy = 0.25
			elif event.key == pygame.K_UP:
				dx = 0
				dy = -0.25
			elif event.key == pygame.K_LEFT:
				dy = 0
				dx = -0.25
			elif event.key == pygame.K_RIGHT:
				dy = 0
				dx = 0.25
	
	#pygame.draw.rect(canvas, BLACK, (snakeSegmentLocations[0].posx + dx, snakeSegmentLocations[0].posy + dy, snakeSegmentLocations[0].size, snakeSegmentLocations[0].size))
	
	for i, segment in enumerate(snakeSegmentLocations):
		#Moving the head
		print(len(snakeSegmentLocations))
		if(i == 0):
			segment.posx += dx
			segment.posy += dy
			#Boundary check

			if(segment.posx < 0 or segment.posx > resolution):
				exit(0)
			elif segment.posy < 0 or segment.posy > resolution:
				exit(0)
			pygame.draw.rect(canvas, BLACK, (segment.posx, segment.posy, segment.size, segment.size))
		if(0 < i < len(snakeSegmentLocations) -1):
			#snakeSegmentLocations[i] = snakeSegmentLocations[i- 1]
			#segment = snakeSegmentLocations[i]
			snakeSegmentLocations[i].posx = snakeSegmentLocations[i- 1].posx
			snakeSegmentLocations[i].posy = snakeSegmentLocations[i- 1].posy
			pygame.draw.rect(canvas, BLACK, (snakeSegmentLocations[i].posx, snakeSegmentLocations[i].posy, snakeSegmentLocations[i].size, snakeSegmentLocations[i].size))



def appleUpdate():
	if(len(appleLocations) == 0):
		appleLocations.append(Apple(random.randint(0, resolution), random.randint(0, resolution), 10))
	else:
		for apple in appleLocations:
			distance = math.sqrt((apple.posx-snakeSegmentLocations[0].posx)**2 + (apple.posy-snakeSegmentLocations[0].posy)**2)
			if(distance < 10):
				appleLocations.remove(apple)
			else:
				pygame.draw.rect(canvas, RED, (apple.posx, apple.posy, apple.size, apple.size))

