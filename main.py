from globals import *
from setup import *
from update import *
from segment import *
from apple import *	

def main():
	while True:
		snakeUpdate()
		appleUpdate()
		
		pygame.display.update()


if __name__ == '__main__':
	main()