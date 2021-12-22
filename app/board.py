
from app.square import Square

# if a single player has any of these combination of squares, they win:
WINNING_COMBINATIONS = [
    ["A1", "B1", "C1"], # [0,1,2], # Row 1
    ["A2", "B2", "C2"], # [3,4,5], # Row 2
    ["A3", "B3", "C3"], # [6,7,8], # Row 3
    ["A1", "A2", "A3"], # [1,4,7], # Column A
    ["B1", "B2", "B3"], # [2,5,8], # Column B
    ["C1", "C2", "C3"], # [3,6,9], # Column C
    ["A3", "B2", "C1"], # [1,5,9], # Diagonal ASC
    ["A1", "B2", "C3"], # [3,5,7], # Diagonal DESC
]

class Board:
    def __init__(self):
        self.squares = [
            Square("A1"), Square("B1"), Square("C1"),
            Square("A2"), Square("B2"), Square("C2"),
            Square("A3"), Square("B3"), Square("C3"),
        ]

    def __repr__(self):
        return f"""
                A   B   C

            1   {self.get_square('A1').player_label} | {self.get_square('B1').player_label} | {self.get_square('C1').player_label}
               -----------
            2   {self.get_square('A2').player_label} | {self.get_square('B2').player_label} | {self.get_square('C2').player_label}
               -----------
            3   {self.get_square('A3').player_label} | {self.get_square('B3').player_label} | {self.get_square('C3').player_label}

        """

    @property
    def selectable_squares(self):
        return [square for square in self.squares if not square.player_name]

    def get_square(self, square_name):
        # todo: change to a dictionary-based lookup approach for additional computational efficiency, as necessary
        # ... which would require changing the initial structure of self.squares
        return [square for square in self.squares if square.name == square_name][0]

    def set_square(self, square_name, player_name):
        square = self.get_square(square_name)
        if not square.player_name:
            square.player_name = player_name

    def get_squares(self, square_names):
        return [square for square in self.squares if square.name in square_names]

    @property
    def winning_player_name(self):
        for square_names in WINNING_COMBINATIONS:
            squares = self.get_squares(square_names)
            player_names = [square.player_name for square in squares] #> ['X', None, None]
            # if the same player controls all three squares:
            if len(player_names) == 3 and len(list(set(player_names))) == 1:
                winning_player = player_names[0]
                return winning_player
        return None



if __name__ == "__main__":
    board = Board()
    #print(board)
    board.set_square("A1", "X")
    board.set_square("C2", "O")
    board.set_square("B1", "X")
    board.set_square("B2", "O")
    board.set_square("C1", "X")
    print(board)

    print(board.selectable_squares)
