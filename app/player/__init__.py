


#from app.player import HumanPlayer, ComputerPlayer, MinimaxPlayer, MinimaxABPlayer
#
#def set_player(letter, strategy):
#    """
#    This is a high-level interface into player selection.
#
#    Params :
#
#        letter (str) : "X" or "O"
#
#        strategy (str) : what kind of player to create
#
#    """
#    if strategy == "HUMAN":
#        return HumanPlayer(letter)
#    elif strategy in ["RANDOM", "COMPUTER", "EASY"]:
#        return ComputerPlayer(letter)
#    elif strategy in ["MINIMAX"]:
#        return MinimaxPlayer(letter)
#    elif strategy in ["MINIMAX-AB", "FAST", "HARD"]:
#        return MinimaxABPlayer(letter)
#
#
## shortcut for importing the individual player classes from here if you want
## for example from app.player import ComputerPlayer
#__all__ = [
#    "set_player", "HumanPlayer", "ComputerPlayer", "MinimaxPlayer", "MinimaxABPlayer"
#]


# there are some circular dependency issues here?
