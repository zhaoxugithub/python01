import pygame
from constants import *

class Board:
    def __init__(self):
        self.pieces = []
        self.setup_pieces()

    def setup_pieces(self):
        # Initialize the board with pieces
        # Red pieces (bottom)
        piece_layout = {
            'red': [
                ('車', 0, 9), ('馬', 1, 9), ('相', 2, 9), ('仕', 3, 9),
                ('帥', 4, 9), ('仕', 5, 9), ('相', 6, 9), ('馬', 7, 9),
                ('車', 8, 9), ('炮', 1, 7), ('炮', 7, 7),
                ('兵', 0, 6), ('兵', 2, 6), ('兵', 4, 6), ('兵', 6, 6), ('兵', 8, 6)
            ],
            'black': [
                ('車', 0, 0), ('馬', 1, 0), ('象', 2, 0), ('士', 3, 0),
                ('將', 4, 0), ('士', 5, 0), ('象', 6, 0), ('馬', 7, 0),
                ('車', 8, 0), ('炮', 1, 2), ('炮', 7, 2),
                ('卒', 0, 3), ('卒', 2, 3), ('卒', 4, 3), ('卒', 6, 3), ('卒', 8, 3)
            ]
        }

        for color, pieces in piece_layout.items():
            for name, x, y in pieces:
                self.pieces.append(Piece(name, color, x, y))

    def get_piece(self, x, y):
        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                return piece
        return None

    def is_valid_move(self, piece, new_x, new_y):
        # Basic movement validation
        if not (0 <= new_x <= 8 and 0 <= new_y <= 9):
            return False

        target = self.get_piece(new_x, new_y)
        if target and target.color == piece.color:
            return False

        # TODO: Implement specific piece movement rules
        return True

    def move_piece(self, piece, new_x, new_y):
        target = self.get_piece(new_x, new_y)
        if target:
            self.pieces.remove(target)
        piece.x = new_x
        piece.y = new_y

    def draw(self, screen):
        # Draw board background
        pygame.draw.rect(screen, BOARD_COLOR,
                        (BOARD_MARGIN, BOARD_MARGIN,
                         CELL_SIZE * 8, CELL_SIZE * 9))

        # Draw grid lines
        for i in range(10):
            # Horizontal lines
            start_y = BOARD_MARGIN + i * CELL_SIZE
            pygame.draw.line(screen, BLACK,
                           (BOARD_MARGIN, start_y),
                           (BOARD_MARGIN + 8 * CELL_SIZE, start_y))

        for i in range(9):
            # Vertical lines
            start_x = BOARD_MARGIN + i * CELL_SIZE
            pygame.draw.line(screen, BLACK,
                           (start_x, BOARD_MARGIN),
                           (start_x, BOARD_MARGIN + 9 * CELL_SIZE))

        # Draw pieces
        for piece in self.pieces:
            piece.draw(screen)