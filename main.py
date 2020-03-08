from globals import *
from update import *
import time
clock = pygame.time.Clock()
def main():
	while True:
		snakeUpdate()
		appleUpdate()
		
		pygame.display.update()
		#time.sleep(0.075)
		clock.tick(10)


if __name__ == '__main__':
	main()