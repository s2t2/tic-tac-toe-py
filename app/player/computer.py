import random

from .base import Player

class ComputerPlayer(Player):
    def __init__(self, letter, name=None, player_type=None):
        player_type = player_type or "RANDOM"
        super().__init__(name=name, letter=letter, player_type=player_type)

    def select_square(self, board):
        print("PLAYER", self.letter, "THINKING...")
        return self.select_random_square(board)

    def select_random_square(self, board):
        random_square = random.choice(board.selectable_squares)
        return random_square.name
