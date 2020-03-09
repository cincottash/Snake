from globals import *
from setup import *

import sys
import random

try:
	resolution = int(sys.argv[1])
except IndexError:
	print("Incorrect argument count, usage is: python main.py 'resolution'")
	exit(0)

pygame.init()

canvas = pygame.display.set_mode((resolution,resolution))

snakeSegmentLocations.append([resolution/2, resolution/2])
#snakeSegmentLocations.append([resolution/2, resolution/2])


appleLocation.append([random.randint(snakeSize, resolution-snakeSize), random.randint(snakeSize, resolution-snakeSize)])