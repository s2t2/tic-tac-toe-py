


class Move:

    def __init__(self, board, active_player, selected_square):
        """
        Params

            board (Board) the initial board state before the player made the move

            active_player (str) the letter of the player who made the move ("X" or "O")

            selected_square (str) the name of the square the player selected (e.g "A1")
        """
        self.board = board
        self.active_player = active_player
        self.selected_square = selected_square

    def __repr__(self):
        return f"<Move '{self.active_player}' to {self.selected_square} >"
