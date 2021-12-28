



class Player:
    """
    A base for other player classes to inherit from and implement their own strategies.
    """
    def __init__(self, letter, name=None, player_type=None):
        self.letter = str(letter)[0].upper() # like "X" or "O"
        self.name = name or f"Player {self.letter}" # like "Player X"
        self.player_type = player_type # "HUMAN", "COMPUTER", etc.

    def select_square(self, board=None):
        raise NotImplementedError("Implement this method. It should optionally accept a board object. And return the name of the square as a string.")
