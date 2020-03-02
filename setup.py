from globals import *
from segment import *
import sys

try:
	resolution = int(sys.argv[1])
except IndexError:
	print("Incorrect argument count, usage is: python main.py 'resolution'")
	exit(0)

pygame.init()

canvas = pygame.display.set_mode((resolution,resolution))

snakeSegmentLocations = []

snakeSegmentLocations.append(snakeSegment(resolution/2, resolution/2, 10))