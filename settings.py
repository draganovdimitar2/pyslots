import os
from random import randint

BASE_DIR = os.path.dirname(__file__)
IMAGE_DIR = os.path.join(BASE_DIR, "image", "symbols")
COINS_DIR = os.path.join(BASE_DIR, "image", "coins")

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
    "club": os.path.join(IMAGE_DIR, "10.png"),
    "seven": os.path.join(IMAGE_DIR, "11.png"),
    "cherry": os.path.join(IMAGE_DIR, "12.png"),
    "bar": os.path.join(IMAGE_DIR, "13.png"),
    "grape": os.path.join(IMAGE_DIR, "14.png")
}

coins = [
    os.path.join(COINS_DIR, "coin_1.png"),
    os.path.join(COINS_DIR, "coin_2.png"),
    os.path.join(COINS_DIR, "coin_3.png"),
    os.path.join(COINS_DIR, "coin_4.png"),
    os.path.join(COINS_DIR, "coin_5.png"),
    os.path.join(COINS_DIR, "coin_6.png")
]

# if you add more symbols, winning chances will become lower
weighted_symbols = [  # currently using only 6 symbols, you can remove or add more to increase\decrease winning chance
    "cherry", "cherry", "cherry", "cherry", "cherry", "cherry",
    'seven','seven','seven',  "seven", "seven", "seven", "seven", "seven", "seven",
    "cherry", "seven", "bar", "diamond", "clover"
]

# percent as decimal (e.g., 1.2 means 120% of bet)
# If you add more symbols be sure to add them on paytable also
SYMBOL_PAYTABLE = {
    "cherry": 1.2,    # 120% of bet per winning line
    "seven": 10,     # 1000% of bet
    "bar": 5.0,       # 500% of bet
    "diamond": 2.5,  # 250% of bet
    "clover": 1.8     # 180% of bet
}

PAYLINES = [  # You can add your custom lines here
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

MYSTERY_STARTING_AMOUNT = randint(1000, 10000)  # Jackpot will be a random num between 1000 and 10000 each game
# you can modify the mystery ranges based on your own preferences
MYSTERY_START_RANGE = 50
MYSTERY_END_RANGE = 100

MYSTERY_PERCENT_PER_BET = 0.2  # 20 % will go for the jackpot each bet
MYSTERY_CHANCE_INCREASE_PER_BET = 1
