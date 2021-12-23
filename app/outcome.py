
#WIN_REASON = "THREE_IN_A_ROW"
#TIE_REASON = "NO_MORE_SQUARES"
#
#class Outcome:
#    """
#    A decorator / wrapper object for completed game results.
#
#    Does not know how to evaluate results. Just display them.
#    """
#
#    def __init__(self, winner, reason):
#        """
#        Param winner (dict) : like {"player_name": "X", "square_names": ["A1", "B1", "C1"]}
#        """
#        self.winner = winner
#        self.reason = reason
#
#    @property
#    def message(self):
#        if self.reason == TIE_REASON:
#            return "TIE GAME"
#        elif self.winner:
#            return f"{self.game.winning_player_name} WINS!"
#
#    @property
#    def winning_player_name(self):
#        try:
#            return self.winner["player_name"]
#        except:
#            return None
#
#    @property
#    def winning_square_names(self):
#        try:
#            return self.winner["square_names"]
#        except:
#            return None
#
#    def to_dict(self):
#        return {
#            "reason": self.reason,
#            "message": self.message,
#            "winning_player_name": self.winning_player_name,
#            "winning_square_names": self.winning_square_names
#        }
#
