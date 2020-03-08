from globals import *
from update import *

def main():
	while True:
		snakeUpdate()
		appleUpdate()
		
		pygame.display.update()


if __name__ == '__main__':
	main()