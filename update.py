from globals import *
from setup import *
import math
global foundApple
global dy
global dx 

foundApple = False
dy = 0
dx = 0

def snakeUpdate():
	#print(len(snakeSegmentLocations))
	global dy
	global dx
	global foundApple
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
				dx = -0.25
				dy = 0
			elif event.key == pygame.K_RIGHT:
				dx = 0.25
				dy = 0
	 
	for i,coordinate in enumerate(snakeSegmentLocations):
		#Moving the head of the snake
		if(i == 0):
			snakeSegmentLocations[i][0] += dx
			snakeSegmentLocations[i][1] += dy
			#Boundary check

			if(snakeSegmentLocations[i][0] < 0 or snakeSegmentLocations[i][0] > resolution):
				exit(0)
			elif snakeSegmentLocations[i][1] < 0 or snakeSegmentLocations[i][1] > resolution:
				exit(0)

			#Add growth
			if(foundApple):
				#Moving down
				if(dx == 0 and dy == 0.25):
					snakeSegmentLocations.insert(0, [snakeSegmentLocations[0][0], snakeSegmentLocations[0][1] + 10])
				#Moving up
				elif(dx == 0 and dy == -0.25):
					snakeSegmentLocations.insert(0, [snakeSegmentLocations[0][0], snakeSegmentLocations[0][1] - 10])
				#Moving left
				elif(dx == -0.25 and dy == 0):
					snakeSegmentLocations.insert(0, [snakeSegmentLocations[0][0] - 10, snakeSegmentLocations[0][1]])
				#Moving right
				elif(dx == 0.25 and dy == 0):
					snakeSegmentLocations.insert(0, [snakeSegmentLocations[0][0] + 10, snakeSegmentLocations[0][1]])
		else:
			snakeSegmentLocations[i][0] = resolution/2
			snakeSegmentLocations[i][1] = resolution/2

		pygame.draw.rect(canvas, BLACK, (snakeSegmentLocations[i][0], snakeSegmentLocations[i][1], 10, 10))


def appleUpdate():
	global foundApple
	if(len(appleLocation) == 0):
		appleLocation.append([random.randint(11, resolution-11), random.randint(11, resolution-11)])
		foundApple = False
	else:
		for apple in appleLocation:
			distance = math.sqrt((apple[0]-snakeSegmentLocations[0][0])**2 + (apple[1]-snakeSegmentLocations[0][1])**2)
			if(distance < 10):
				appleLocation.remove(apple)
				foundApple = True
			else:
				pygame.draw.rect(canvas, RED, (apple[0], apple[1], 10, 10))

