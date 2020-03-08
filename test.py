import pygame
import time
import random
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
canvasWidth = 600
canvasHeight = 400
 
canvas = pygame.display.set_mode((canvasWidth, canvasHeight))
 
clock = pygame.time.Clock()
 
snakeSize = 10
snakeSpeed = 15

def drawSnake(snakeSegmentList):
    for coordinate in snakeSegmentList:
        pygame.draw.rect(canvas, black, [coordinate[0], coordinate[1], snakeSize, snakeSize])
 
def gameLoop():
	game_over = False
	game_close = False

	x1 = canvasWidth / 2
	y1 = canvasHeight / 2

	dx = 0
	dy = 0

	snakeSegmentList = []
	snakeLength = 1

	foodx = round(random.randrange(0, canvasWidth - snakeSize) / 10.0) * 10.0
	foody = round(random.randrange(0, canvasHeight - snakeSize) / 10.0) * 10.0

	while not game_over:

	    if game_close == True:
	    	exit(0)

	    for event in pygame.event.get():
	        if event.type == pygame.KEYDOWN:
	            if event.key == pygame.K_LEFT:
	                dx = -snakeSize
	                dy = 0
	            elif event.key == pygame.K_RIGHT:
	                dx = snakeSize
	                dy = 0
	            elif event.key == pygame.K_UP:
	                dy = -snakeSize
	                dx = 0
	            elif event.key == pygame.K_DOWN:
	                dy = snakeSize
	                dx = 0
	    #Checking if our snake is within the screen bounds
	    if x1 >= canvasWidth or x1 < 0 or y1 >= canvasHeight or y1 < 0:
	        game_close = True
	    
	    x1 += dx
	    y1 += dy
	    
	    canvas.fill(blue)
	    
	    #Drawing the food
	    pygame.draw.rect(canvas, green, [foodx, foody, snakeSize, snakeSize])
	    
	    newSegment = []
	    newSegment.append(x1)
	    newSegment.append(y1)
	    snakeSegmentList.append(newSegment)
	    
	    if len(snakeSegmentList) > snakeLength:
	        del snakeSegmentList[0]

	    #Check if we have collided with ourselves.
	    for x in snakeSegmentList[:-1]:
	        if x == snakeHead:
	            game_close = True

	    drawSnake(snakeSegmentList)


	    pygame.display.update()

	    if x1 == foodx and y1 == foody:
	        foodx = round(random.randrange(0, canvasWidth - snakeSize) / 10.0) * 10.0
	        foody = round(random.randrange(0, canvasHeight - snakeSize) / 10.0) * 10.0
	        snakeLength += 1

	    clock.tick(snakeSpeed)

	pygame.quit()
	quit()
 
 
gameLoop()