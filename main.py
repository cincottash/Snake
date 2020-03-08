from globals import *
from update import *
import time
def main():
	while True:
		snakeUpdate()
		appleUpdate()
		
		pygame.display.update()
		#time.sleep(0.0025)


if __name__ == '__main__':
	main()