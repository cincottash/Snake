from globals import *
from segment import *
from apple import *
from setup import *

global dy
global dx 

dy = 0
dx = 0

def snakeUpdate():
	#print(len(snakeSegmentLocations))
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
	 
	for i in range(len(snakeSegmentLocations)):
		#Moving the head of the snake
		if(i == 0):
			
			snakeSegmentLocations[i].posx += dx
			snakeSegmentLocations[i].posy += dy
			#Boundary check

			if(snakeSegmentLocations[i].posx < 0 or snakeSegmentLocations[i].posx > resolution):
				exit(0)
			elif snakeSegmentLocations[i].posy < 0 or snakeSegmentLocations[i].posy > resolution:
				exit(0)
			pygame.draw.rect(canvas, BLACK, (snakeSegmentLocations[i].posx, snakeSegmentLocations[i].posy, snakeSegmentLocations[i].size, snakeSegmentLocations[i].size))


def appleUpdate():
	if(len(appleLocation) == 0):
		appleLocation.append(Apple(random.randint(0, resolution), random.randint(0, resolution), 10))
	else:
		for apple in appleLocation:
			distance = math.sqrt((apple.posx-snakeSegmentLocations[0].posx)**2 + (apple.posy-snakeSegmentLocations[0].posy)**2)
			if(distance < 10):
				appleLocation.remove(apple)
			else:
				pygame.draw.rect(canvas, RED, (apple.posx, apple.posy, apple.size, apple.size))

