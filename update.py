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
		
	
	for i, segment in enumerate(snakeSegmentLocations):
		print(i)
		#Moving the head of the snake
		if(i == 0):
			segment.posx += dx
			segment.posy += dy
			#Boundary check

			if(segment.posx < 0 or segment.posx > resolution):
				exit(0)
			elif segment.posy < 0 or segment.posy > resolution:
				exit(0)
			#pygame.draw.rect(canvas, BLACK, (segment.posx, segment.posy, segment.size, segment.size))
		#Different logic for moving the rest of the segments that aren't the head
		else:
			# segment.posx = snakeSegmentLocations[i - 1].posx
			# segment.posy = snakeSegmentLocations[i - 1].posy
			segment = snakeSegment(snakeSegmentLocations[i - 1].posx, snakeSegmentLocations[i - 1].posy, 10)
			# segment.posx += dx
			# segment.posy += dy
			if(segment.posx < 0 or segment.posx > resolution):
				exit(0)
			elif segment.posy < 0 or segment.posy > resolution:
				exit(0)
			#pygame.draw.rect(canvas, BLACK, (segment.posx, segment.posy, segment.size, segment.size))
	for segment in snakeSegmentLocations:
		pygame.draw.rect(canvas, BLACK, (segment.posx, segment.posy, segment.size, segment.size))



def appleUpdate():
	if(len(appleLocation) == 0):
		appleLocation.append(Apple(random.randint(0, resolution), random.randint(0, resolution), 10))
	else:
		for apple in appleLocation:
			distance = math.sqrt((apple.posx-snakeSegmentLocations[0].posx)**2 + (apple.posy-snakeSegmentLocations[0].posy)**2)
			if(distance < 10):
				appleLocation.remove(apple)
				#Determine the new coords for which to place the new segment
				newPosx = snakeSegmentLocations[len(snakeSegmentLocations)-1].posx
				newPosy = snakeSegmentLocations[len(snakeSegmentLocations)-1].posy

				#Moving down
				if(dx == 0 and dy == 0.25):
					snakeSegmentLocations.append(snakeSegment(newPosx, newPosy-11, 10))
				#Moving up
				elif(dx == 0 and dy == -0.25):
					snakeSegmentLocations.append(snakeSegment(newPosx, newPosy+11, 10))
				#Moving left
				elif(dx == -0.25 and dy == 0):
					snakeSegmentLocations.append(snakeSegment(newPosx+11, newPosy, 10))
				elif(dx == 0.25 and dy == 0):
					snakeSegmentLocations.append(snakeSegment(newPosx-11, newPosy, 10))
			else:
				pygame.draw.rect(canvas, RED, (apple.posx, apple.posy, apple.size, apple.size))

