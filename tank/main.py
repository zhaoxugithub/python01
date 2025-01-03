import pygame
from game import Game
from constants import WINDOW_WIDTH, WINDOW_HEIGHT, TITLE

def main():
    pygame.init()
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption(TITLE)
    
    game = Game(screen)
    game.run()

if __name__ == "__main__":
    main()