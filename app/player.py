

import random

class Player:
    def __init__(self, letter, name=None, player_type=None):
        self.letter = str(letter)[0].upper() # like "X" or "O"
        self.name = name or f"Player {self.letter}" # like "Player X"
        self.player_type = player_type # "HUMAN" or "COMPUTER"

    def select_square(self, board=None):
        raise NotImplementedError("Implement this method. It should optionally accept a board object. And return the name of the square as a string.")


class HumanPlayer(Player):
    def __init__(self, letter, name=None):
        super().__init__(name=name, letter=letter, player_type="HUMAN")

    def select_square(self, board=None):
        return input(f"PLAYER {self.letter} PLEASE SELECT A SQUARE (i.e. 'A1'): ").upper()


class ComputerPlayer(Player):
    def __init__(self, letter, name=None, strategy="RANDOM"):
        self.strategy = strategy
        super().__init__(name=name, letter=letter, player_type="COMPUTER")

    def select_square(self, board):
        #if self.strategy == "RANDOM":
        #    return random.choice(board.selectable_squares)
        #elif self.strategy == "MINIMAX":
        #    return self.minimax(board)

        random_square = random.choice(board.selectable_squares)
        return random_square.name
