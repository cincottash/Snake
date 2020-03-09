from globals import *
from update import *
import time
clock = pygame.time.Clock()

def main():
	while True:
		snakeUpdate()
		pygame.display.update()
		appleUpdate()
		pygame.display.update()
		

		clock.tick(15)


if __name__ == '__main__':
	main()