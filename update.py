from globals import *
from setup import *
from exceptions import *
import math
global foundApple
global direction
global dy
global dx 

foundApple = False
direction = "None"
dy = 0
dx = 0

def draw(snakeSegmentLocations):
	for segment in snakeSegmentLocations:
		pygame.draw.rect(canvas, BLACK, (segment[0], segment[1], snakeSize, snakeSize))

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
					dy = snakeSize
					direction = "Down"
			elif event.key == pygame.K_UP:
				if(direction != "Down"):
					dx = 0
					dy = -snakeSize
					direction = "Up"
			elif event.key == pygame.K_LEFT:
				if(direction != "Right"):
					dx = -snakeSize
					dy = 0
					direction = "Left"
			elif event.key == pygame.K_RIGHT:
				if(direction != "Left"):
					dx = snakeSize
					dy = 0
					direction = "Right"

	#Moving the head of the snake
	snakeSegmentLocations[0][0] += dx
	snakeSegmentLocations[0][1] += dy
	
	#Boundary check

	if(snakeSegmentLocations[0][0] < 0 or snakeSegmentLocations[0][0] > resolution - snakeSize/2):
		exit(0)
	elif (snakeSegmentLocations[0][1] < 0 or snakeSegmentLocations[0][1] > resolution - snakeSize/2):
		exit(0)

	if(foundApple):
		snakeSegmentLocations.insert(0,[snakeSegmentLocations[0][0], snakeSegmentLocations[0][1]])
		foundApple = False

	elif(len(snakeSegmentLocations) > 1):
		snakeSegmentLocations.pop()
		snakeSegmentLocations.insert(0, [snakeSegmentLocations[0][0], snakeSegmentLocations[0][1]])
	
	#Check for overlap on yourself
	for i,segment in enumerate(snakeSegmentLocations):
		if(segment == snakeSegmentLocations[0] and (i > 1)):
			exit(0)
	
	draw(snakeSegmentLocations)



def appleUpdate():
	global foundApple
	if(len(appleLocation) == 0):
		appleLocation.append([random.randint(snakeSize, resolution-snakeSize), random.randint(snakeSize, resolution-snakeSize)])
		
	else:
		for apple in appleLocation:
			distance = math.sqrt((apple[0]-snakeSegmentLocations[0][0])**2 + (apple[1]-snakeSegmentLocations[0][1])**2)
			if(distance < snakeSize):
				appleLocation.remove(apple)
				foundApple = True
			else:
				pygame.draw.rect(canvas, RED, (apple[0], apple[1], snakeSize, snakeSize))

