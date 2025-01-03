import pygame
from constants import *

class Piece:
    def __init__(self, name, color, x, y):
        self.name = name
        self.color = color
        self.x = x
        self.y = y
        
        # Initialize font for piece rendering
        self.font = pygame.font.SysFont('simhei', 48)

    def draw(self, screen):
        x = self.x * CELL_SIZE + BOARD_MARGIN
        y = self.y * CELL_SIZE + BOARD_MARGIN
        
        # Draw piece background
        pygame.draw.circle(screen, (255, 255, 255),
                         (x + CELL_SIZE // 2, y + CELL_SIZE // 2),
                         PIECE_SIZE // 2)
        pygame.draw.circle(screen, BLACK,
                         (x + CELL_SIZE // 2, y + CELL_SIZE // 2),
                         PIECE_SIZE // 2, 2)
        
        # Draw piece text
        text_color = RED if self.color == 'red' else BLACK
        text = self.font.render(self.name, True, text_color)
        text_rect = text.get_rect(center=(x + CELL_SIZE // 2,
                                        y + CELL_SIZE // 2))
        screen.blit(text, text_rect)