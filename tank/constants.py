import os

# Window settings
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 900
TITLE = "Chinese Chess (象棋)"

# Board settings
BOARD_MARGIN = 50
CELL_SIZE = 76
PIECE_SIZE = 70

# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BOARD_COLOR = (238, 203, 173)

# Asset paths
ASSETS_DIR = "assets"
if not os.path.exists(ASSETS_DIR):
    os.makedirs(ASSETS_DIR)