from globals import *
from segment import *
from apple import *
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

snakeSegmentLocations.append(snakeSegment(resolution/2, resolution/2, 10))

appleLocation.append(Apple(random.randint(11, resolution-11), random.randint(11, resolution-11), 10))