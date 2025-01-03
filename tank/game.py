import pygame
from board import Board
from piece import Piece
from constants import *

class Game:
    def __init__(self, screen):
        self.screen = screen
        self.board = Board()
        self.selected_piece = None
        self.current_player = 'red'  # red goes first
        self.running = True

    def handle_click(self, pos):
        x, y = pos
        board_x = (x - BOARD_MARGIN) // CELL_SIZE
        board_y = (y - BOARD_MARGIN) // CELL_SIZE
        
        if not (0 <= board_x <= 8 and 0 <= board_y <= 9):
            return

        if self.selected_piece is None:
            piece = self.board.get_piece(board_x, board_y)
            if piece and piece.color == self.current_player:
                self.selected_piece = piece
        else:
            if self.board.is_valid_move(self.selected_piece, board_x, board_y):
                self.board.move_piece(self.selected_piece, board_x, board_y)
                self.current_player = 'black' if self.current_player == 'red' else 'red'
            self.selected_piece = None

    def run(self):
        clock = pygame.time.Clock()
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.handle_click(event.pos)

            self.screen.fill((255, 255, 255))
            self.board.draw(self.screen)
            
            if self.selected_piece:
                x = self.selected_piece.x * CELL_SIZE + BOARD_MARGIN
                y = self.selected_piece.y * CELL_SIZE + BOARD_MARGIN
                pygame.draw.rect(self.screen, (0, 255, 0), 
                               (x, y, CELL_SIZE, CELL_SIZE), 2)

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()