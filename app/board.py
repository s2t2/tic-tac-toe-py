
from app.square import Square

class Board:
    """A dumb collection of squares."""

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
    def selectable_squares(self) -> list:
        return [square for square in self.squares if not square.player_name]

    @property
    def out_of_squares(self) -> bool:
        return not any(self.selectable_squares)



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
