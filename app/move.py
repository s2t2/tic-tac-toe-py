


class Move:

    def __init__(self, board_state, active_player, selected_square):
        """
        Params

            board_state (str) the initial board state before the player made the move

            active_player (str) the letter of the player who made the move ("X" or "O")

            selected_square (str) the name of the square the player selected (e.g "A1")
        """
        self.board_state = board_state #> "XX-OO----"
        self.active_player = active_player #> "X"
        self.selected_square = selected_square #> "C1"

    def __repr__(self):
        return f"<Move '{self.active_player}' to {self.selected_square} >"
