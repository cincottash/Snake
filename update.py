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
	global dy
	global dx
	global foundApple
	canvas.fill(WHITE)

	for event in pygame.event.get():	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				dx = 0
				dy = 10
			elif event.key == pygame.K_UP:
				dx = 0
				dy = -10
			elif event.key == pygame.K_LEFT:
				dx = -10
				dy = 0
			elif event.key == pygame.K_RIGHT:
				dx = 10
				dy = 0

	#Moving the head of the snake
	snakeSegmentLocations[0][0] += dx
	snakeSegmentLocations[0][1] += dy
	
	#Boundary check
	if(snakeSegmentLocations[0][0] < 0 or snakeSegmentLocations[0][0] > resolution):
		exit(0)
	elif snakeSegmentLocations[0][1] < 0 or snakeSegmentLocations[0][1] > resolution:
		exit(0)

	#Add growth
	if(foundApple):
		#Moving down
		if(dx == 0 and dy == 10):
			snakeSegmentLocations.insert(0,[snakeSegmentLocations[0][0], snakeSegmentLocations[0][1]])

		#Moving up
		elif(dx == 0 and dy == -10):
			snakeSegmentLocations.insert(0, [snakeSegmentLocations[0][0], snakeSegmentLocations[0][1]])

		#Moving left
		elif(dx == -10 and dy == 0):
			snakeSegmentLocations.insert(0, [snakeSegmentLocations[0][0], snakeSegmentLocations[0][1]])

		#Moving right
		elif(dx == 10 and dy == 0):
			snakeSegmentLocations.insert(0, [snakeSegmentLocations[0][0], snakeSegmentLocations[0][1]])

	#Moving down
	elif(len(snakeSegmentLocations) > 1):
		#print("here")
		if(dx == 0 and dy == 10):
			snakeSegmentLocations.pop()
			snakeSegmentLocations.insert(0, [snakeSegmentLocations[0][0], snakeSegmentLocations[0][1]])
								
		#Moving up
		elif(dx == 0 and dy == -10):
			snakeSegmentLocations.pop()
			snakeSegmentLocations.insert(0, [snakeSegmentLocations[0][0], snakeSegmentLocations[0][1]])
			#snakeSegmentLocations.pop()

		#Moving left
		elif(dx == -10 and dy == 0):
			snakeSegmentLocations.pop()
			snakeSegmentLocations.insert(0, [snakeSegmentLocations[0][0], snakeSegmentLocations[0][1]])
		#Moving right
		elif(dx == 10 and dy == 0):
			snakeSegmentLocations.pop()
			snakeSegmentLocations.insert(0, [snakeSegmentLocations[0][0], snakeSegmentLocations[0][1]])
	draw(snakeSegmentLocations)

def draw(snakeSegmentLocations):
	print(len(snakeSegmentLocations))
	for i,segment in enumerate(snakeSegmentLocations):
		#print("Segment {} location: {}".format(i, segment))
		pygame.draw.rect(canvas, BLACK, (segment[0], segment[1], 10, 10))


def appleUpdate():
	global foundApple
	if(len(appleLocation) == 0):
		appleLocation.append([random.randint(11, resolution-11), random.randint(11, resolution-11)])
		foundApple = False
	else:
		for apple in appleLocation:
			distance = math.sqrt((apple[0]-snakeSegmentLocations[0][0])**2 + (apple[1]-snakeSegmentLocations[0][1])**2)
			if(distance < 15):
				appleLocation.remove(apple)
				foundApple = True
			else:
				pygame.draw.rect(canvas, RED, (apple[0], apple[1], 10, 10))

