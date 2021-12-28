

from app.player import HumanPlayer, ComputerPlayer, MinimaxPlayer, MinimaxABPlayer

def set_player(letter, strategy):
    """
    This is a high-level interface into player selection.

    Params :

        letter (str) : "X" or "O"

        strategy (str) : what kind of player to create

    """
    if strategy == "HUMAN":
        return HumanPlayer(letter)
    elif strategy in ["RANDOM", "COMPUTER", "EASY"]:
        return ComputerPlayer(letter)
    elif strategy in ["MINIMAX"]:
        return MinimaxPlayer(letter)
    elif strategy in ["MINIMAX-AB", "FAST", "HARD"]:
        return MinimaxABPlayer(letter)
