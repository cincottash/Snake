from globals import *
from setup import *
import math
global foundApple
global direction
global dy
global dx 

foundApple = False
direction = "None"
dy = 0
dx = 0

def snakeUpdate():
	global dy
	global dx
	global foundApple
	global direction
	canvas.fill(WHITE)

	for event in pygame.event.get():	
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_DOWN:
				if(direction != "Up"):
					dx = 0
					dy = 15
					direction = "Down"
			elif event.key == pygame.K_UP:
				if(direction != "Down"):
					dx = 0
					dy = -15
					direction = "Up"
			elif event.key == pygame.K_LEFT:
				if(direction != "Right"):
					dx = -15
					dy = 0
					direction = "Left"
			elif event.key == pygame.K_RIGHT:
				if(direction != "Left"):
					dx = 15
					dy = 0
					direction = "Right"

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
		snakeSegmentLocations.insert(0,[snakeSegmentLocations[0][0], snakeSegmentLocations[0][1]])

	elif(len(snakeSegmentLocations) > 1):
		#Moving down
		if(direction == "Down"):
			snakeSegmentLocations.pop()
			snakeSegmentLocations.insert(0, [snakeSegmentLocations[0][0], snakeSegmentLocations[0][1]])
								
		#Moving up
		elif(direction == "Up"):
			snakeSegmentLocations.pop()
			snakeSegmentLocations.insert(0, [snakeSegmentLocations[0][0], snakeSegmentLocations[0][1]])
			#snakeSegmentLocations.pop()

		#Moving left
		elif(direction == "Left"):
			snakeSegmentLocations.pop()
			snakeSegmentLocations.insert(0, [snakeSegmentLocations[0][0], snakeSegmentLocations[0][1]])
		#Moving right
		elif(direction == "Right"):
			snakeSegmentLocations.pop()
			snakeSegmentLocations.insert(0, [snakeSegmentLocations[0][0], snakeSegmentLocations[0][1]])
	#Check for overlap on yourself
	for i,segment in enumerate(snakeSegmentLocations):
		if(segment == snakeSegmentLocations[0] and (i > 1)):
			exit(0)
	
	draw(snakeSegmentLocations)

def draw(snakeSegmentLocations):
	print(len(snakeSegmentLocations))
	for i,segment in enumerate(snakeSegmentLocations):
		pygame.draw.rect(canvas, BLACK, (segment[0], segment[1], 15, 15))


def appleUpdate():
	global foundApple
	if(len(appleLocation) == 0):
		appleLocation.append([random.randint(15, resolution-15), random.randint(15, resolution-15)])
		foundApple = False
	else:
		for apple in appleLocation:
			distance = math.sqrt((apple[0]-snakeSegmentLocations[0][0])**2 + (apple[1]-snakeSegmentLocations[0][1])**2)
			if(distance < 15):
				appleLocation.remove(apple)
				foundApple = True
			else:
				pygame.draw.rect(canvas, RED, (apple[0], apple[1], 15, 15))

