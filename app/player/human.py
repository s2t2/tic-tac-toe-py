

from .base import Player

class HumanPlayer(Player):
    def __init__(self, letter, name=None):
        super().__init__(name=name, letter=letter, player_type="HUMAN")

    def select_square(self, board=None):
        return input(f"PLAYER {self.letter} PLEASE SELECT A SQUARE (i.e. 'A1'): ").upper()
