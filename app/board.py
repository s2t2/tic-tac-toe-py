
#from functools import cache

from app.square import Square

SQUARE_NAMES = [
    "A1", "B1", "C1",
    "A2", "B2", "C2",
    "A3", "B3", "C3",
]

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

class SquareTakenError(ValueError):
    pass

class Board:
    def __init__(self):
        self.squares = [Square(square_name) for square_name in SQUARE_NAMES]
        self._winner = None # a cached value for the eventual winner
        self._outcome = None # a cached value for the eventual outcome

    def __repr__(self):
        return f"""
                A   B   C

            1   {self.get_square('A1').label} | {self.get_square('B1').label} | {self.get_square('C1').label}
               -----------
            2   {self.get_square('A2').label} | {self.get_square('B2').label} | {self.get_square('C2').label}
               -----------
            3   {self.get_square('A3').label} | {self.get_square('B3').label} | {self.get_square('C3').label}

        """

    @property
    def notation(self) -> str:
        """
        Represents the board's current state in simple string format like "-X-O-X-OX".

        Position corresponds with square names ['A1','B1','C1','A2','B2','C2','A3','B3','C3'] and indices [0,1,2,3,4,5,6,7,8].
        """
        return "".join([square.notation for square in self.squares])


    def get_square(self, square_name):
        # todo: change to a dictionary-based lookup approach for additional computational efficiency, as necessary
        # ... which would require changing the initial structure of self.squares
        return [square for square in self.squares if square.name == square_name][0]

    def get_squares(self, square_names):
        return [square for square in self.squares if square.name in square_names]

    def set_square(self, square_name, player_letter):
        square = self.get_square(square_name)
        if square.letter:
            raise SquareTakenError(f"OOPS, square '{square_name}' already taken. please try again...")
        else:
            square.letter = player_letter


    @property
    def selectable_squares(self) -> list:
        return [square for square in self.squares if square.is_selectable]

    @property
    def out_of_squares(self) -> bool:
        return not any(self.selectable_squares)


    @property
    def winner(self):
        if self._winner:
            return self._winner # use cached value to prevent unnecessary calculations

        #print("DETERMINING WINNER")
        for square_names in WINNING_COMBINATIONS:
            squares = self.get_squares(square_names)
            # if the same player controls all three squares:
            letters = [square.letter for square in squares]
            if len(letters) == 3 and len(list(set(letters))) == 1:
                winning_letter = letters[0]
                if winning_letter:
                    self._winner = {"letter": winning_letter, "square_names": square_names} # set cached value for future lookups
                    return self._winner

        return None

    @property
    def outcome(self):
        if self._outcome:
            return self._outcome # use cached value to prevent unnecessary calculations

        winner = self.winner
        if winner:
            self._outcome = {"winner": winner, "reason": "THREE_IN_A_ROW", "message": f"{winner['letter']} WINS!" }
        elif self.out_of_squares:
            self._outcome = {"winner": None, "reason": "NO_MORE_SQUARES", "message": "TIE GAME" }

        return self._outcome


    @property
    def winning_letter(self):
        try:
            return self.winner["letter"]
        except:
            return None

    @property
    def winning_square_names(self):
        try:
            return self.winner["square_names"]
        except:
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

    print(board.outcome)


    #breakpoint()
