


COLS_MAP = {"A": 0, "B": 1 , "C": 2}

def row_col(grid_notation):
    """Params cell notation like "A1",  where and cols are A, B, C and rows are 1, 2, 3

           A | B | C
        1  _ | _ | _
        2  _ | _ | _
        3  _ | _ | _

    """
    grid_notation = grid_notation.upper() #> "A1"
    col, row = list(grid_notation)
    col_idx = COLS_MAP[col]
    row_idx = int(row) - 1
    return row_idx, col_idx


class Board:
    def __init__(self):
        self.grid = [
            [None, None, None], # A1, B1, C1
            [None, None, None], # A2, B2, C2
            [None, None, None]  # A3, B3, C3
        ]

    def __repr__(self):
        return f"""
                A   B   C
               -----------
            1 | {self.grid[0][0] or ' '} | {self.grid[0][1] or ' '} | {self.grid[0][2] or ' '} |
              |-----------|
            2 | {self.grid[1][0] or ' '} | {self.grid[1][1] or ' '} | {self.grid[1][2] or ' '} |
              |-----------|
            3 | {self.grid[2][0] or ' '} | {self.grid[2][1] or ' '} | {self.grid[2][2] or ' '} |
               -----------
        """

    def show(self):
        print("")

        for index, row in enumerate(self.grid):
            if index != 0:
                print("-"*9)

            padded_cells = [cell or " " for cell in row]
            print(" | ".join(padded_cells))

        print("")

    def set_square(self, grid_notation, label):
        r, c = row_col(grid_notation)
        #self.grid[r][c] = label
        if not self.grid[r][c]:
            self.grid[r][c] = label


if __name__ == "__main__":
    board = Board()
    #print(board)
    board.set_square("A1", "X")
    board.set_square("C2", "O")
    board.set_square("B1", "X")
    board.set_square("B2", "O")
    board.set_square("C1", "X")
    print(board)

    #print(board.move_history)
