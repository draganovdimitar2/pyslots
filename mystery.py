from random import randint
from settings import *

class Mystery:
    def __init__(self):
        self.mystery_amount = MYSTERY_STARTING_AMOUNT
        self.mystery_target_price = randint(MYSTERY_START_RANGE, MYSTERY_END_RANGE) # when mystery will be triggered
        self.counter = 0
        self.is_triggered = False

    def mystery_checker(self):
        if self.counter >= self.mystery_target_price:
            # reset data
            self.is_triggered = True
            self.counter = 0
            self.mystery_target_price = randint(MYSTERY_START_RANGE, MYSTERY_END_RANGE)
            return True
        self.is_triggered = False
        return False

    def increment_mystery_amount(self, player_bet):
        self.mystery_amount += player_bet * MYSTERY_PERCENT_PER_BET # percent of each players bet will go to the mystery
        self.counter += MYSTERY_CHANCE_INCREASE_PER_BET

