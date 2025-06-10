import os

BASE_DIR = os.path.dirname(__file__)
IMAGE_DIR = os.path.join(BASE_DIR, "image", "symbols")

BACKGROUND = "image/background.jpg"
FPS = 120
GAME_HEIGHT = 600
UI_HEIGHT = 80
HEIGHT = GAME_HEIGHT + UI_HEIGHT  # 30px are used for the text font
UI_FONT_POS_Y = HEIGHT - (UI_HEIGHT // 2 - 10)
WIDTH = 1200

SYMBOL_WIDTH = 240
SYMBOL_HEIGHT = 200
START_X, START_Y = 0, -SYMBOL_HEIGHT // 2
GAME_INDICES = [1, 2, 3]

DELAY_FOR_EACH_REEL = 200

# TEXT
TEXT_COLOR = "white"
UI_FONT = "font/kidspace.ttf"
UI_FONT_SIZE = 25
WIN_FONT_SIZE = 65

symbols = {
    "star": os.path.join(IMAGE_DIR, "1.png"),
    "bell": os.path.join(IMAGE_DIR, "2.png"),
    "bag": os.path.join(IMAGE_DIR, "3.png"),
    "heart": os.path.join(IMAGE_DIR, "4.png"),
    "lemon": os.path.join(IMAGE_DIR, "5.png"),
    "clover": os.path.join(IMAGE_DIR, "6.png"),
    "diamond": os.path.join(IMAGE_DIR, "7.png"),
    "spade": os.path.join(IMAGE_DIR, "8.png"),
    "present": os.path.join(IMAGE_DIR, "9.png"),
    "club": os.path.join(IMAGE_DIR, "10.png")
}

# if you add more symbols, winning chances will become lower
weighted_symbols = [  # currently using only 5 symbols
    "star", "star", "star", "star",
    "bell", "bell", "bell", "bell",
    "clover", "clover", "clover", "clover",
    "diamond",
    "lemon",
    # "clover",
    # "diamond",
    # "spade",
    # "present",
    # "club"

]

PAYLINES = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    [(0, 0), (1, 1), (2, 2)],
    [(2, 0), (1, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2), (1, 3), (1, 4)],  # second_row
    [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4)],  # first_row
    [(2, 0), (2, 1), (2, 2), (2, 3), (2, 4)],  # third row
    [(0, 0), (1, 1), (2, 2), (1, 3), (0, 4)],  # V - shape
    [(2, 0), (1, 1), (0, 2), (1, 3), (2, 4)],  # V - shape upside down
    [(0, 0), (0, 1), (1, 2), (0, 3), (0, 4)],
    [(2, 0), (2, 1), (1, 2), (2, 3), (2, 4)],
    [(1, 0), (2, 1), (2, 2), (2, 3), (1, 4)],
    [(2, 0), (1, 1), (2, 2), (1, 3), (2, 4)],
    [(1, 0), (1, 1), (0, 2), (1, 3), (1, 4)],
    [(1, 0), (1, 1), (2, 2), (1, 3), (1, 4)],
    [(1, 0), (0, 1), (1, 2), (0, 3), (1, 4)],
    [(1, 0), (2, 1), (1, 2), (2, 3), (1, 4)],
    [(0, 0), (1, 1), (1, 2), (1, 3), (0, 4)],
    [(0, 0), (0, 1), (2, 2), (0, 3), (0, 4)],
    [(2, 0), (2, 1), (0, 2), (2, 3), (2, 4)],
    [(1, 0), (2, 1), (0, 2), (2, 3), (1, 4)],
    [(0, 0), (0, 1), (0, 2), (1, 3), (2, 4)],
    [(2, 0), (2, 1), (2, 2), (1, 3), (0, 4)],
    [(0, 0), (1, 1), (2, 2), (2, 3), (2, 4)],
    [(2, 0), (2, 1), (1, 2), (0, 3), (0, 4)],
    [(0, 0), (0, 1), (1, 2), (2, 3), (1, 4)],
    [(2, 0), (2, 1), (1, 2), (0, 3), (1, 4)],
    [(1, 0), (1, 1), (1, 2), (1, 3), (0, 4)],
    [(1, 0), (1, 1), (1, 2), (1, 3), (2, 4)],
    [(0, 0), (1, 1), (0, 2), (1, 3), (2, 4)],
    [(2, 0), (2, 1), (2, 2), (2, 3), (1, 4)],
    [(1, 0), (2, 1), (2, 2), (2, 3), (2, 4)],
    [(1, 0), (0, 1), (0, 2), (0, 3), (0, 4)],
    [(1, 0), (1, 1), (0, 2), (0, 3), (0, 4)],
    [(1, 0), (1, 1), (2, 2), (2, 3), (2, 4)],
    [(0, 0), (1, 1), (1, 2), (1, 3), (2, 4)]
]
