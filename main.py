from globals import *
from setup import *
from update import *
from segment import *

def main():
	while True:
		snakeUpdate()
		
		pygame.display.update()


if __name__ == '__main__':
	main()