

import random

class Player:
    def __init__(self, letter, name=None, player_type=None):
        self.letter = str(letter)[0].upper() # like "X" or "O"
        self.name = name or f"Player {self.letter}" # like "Player X"
        self.player_type = player_type # "HUMAN" or "COMPUTER"

    def select_square(self, board=None):
        raise NotImplementedError("Implement this method. It should optionally accept a board object. And return the name of the square as a string.")


class HumanPlayer(Player):
    def __init__(self, letter, name=None):
        super().__init__(name=name, letter=letter, player_type="HUMAN")

    def select_square(self, board=None):
        return input(f"PLAYER {self.letter} PLEASE SELECT A SQUARE (i.e. 'A1'): ").upper()


class ComputerPlayer(Player):
    def __init__(self, letter, name=None, strategy="RANDOM"):
        self.strategy = strategy
        super().__init__(name=name, letter=letter, player_type="COMPUTER")

    def select_square(self, board):
        #if self.strategy == "RANDOM":
        #    return random.choice(board.selectable_squares)
        #elif self.strategy == "MINIMAX":
        #    return self.minimax(board)

        random_square = random.choice(board.selectable_squares)
        return random_square.name

















import copy
from math import inf

OPPOSITE_LETTER = {"X": "O", "O": "X"} # todo: make more dynamic

class MinimaxPlayer(Player):
    # https://www.youtube.com/watch?v=J1GoI5WHBto
    # https://www.youtube.com/watch?v=STjW3eH0Cik
    # https://www.youtube.com/watch?v=fT3YWCKvuQE

    def __init__(self, letter, name=None):
        super().__init__(name=name, letter=letter, player_type="COMPUTER")

    def select_square(self, board):
        if len(board.selectable_squares) == 9:
            random_square = random.choice(board.selectable_squares)
            return random_square.name

        best_square = None
        best_score = -inf
        for square in board.selectable_squares:
            # make a new board (so the original isn't affected)
            new_board = copy.deepcopy(board)

            # simulate a move on the game board
            new_board.set_square(square.name, self.letter)

            # get a value for this move
            score = self.minimax(new_board, depth=0, maximizing=False) # after setting the square ourselves, we allow the opposing player to take the next turn

            # update best scorer, and keep track of which square is best
            if score > best_score:
                best_score = score
                best_square = square

        return best_square.name






    def minimax(self, board, depth=0, maximizing=True):

        if maximizing == True:
            letter = self.letter
        else:
            letter = OPPOSITE_LETTER[self.letter]
        #print(board)

        #print("-"*(depth+1))

        if board.outcome:
            #print("-"*(depth+1), "OUTCOME:", board.outcome["message"], "IN", depth)

            if board.winning_letter == letter:
                return 1 * (depth+1)
            elif board.winning_letter != letter:
                return -1 * (depth+1)
            else:
                return 0

        if maximizing == True:

            best_score = -inf
            for square in board.selectable_squares:
                # make a new board (so the original isn't affected)
                new_board = copy.deepcopy(board)

                # simulate a move on the game board
                new_board.set_square(square.name, letter)
                #print("-"*(depth+1), letter, square.name)

                # get a value for this move
                score = self.minimax(new_board, depth=depth+1, maximizing=False)

                # keep track of best score
                best_score = max(score, best_score)

            return best_score

        else:

            best_score = inf
            for square in board.selectable_squares:
                # make a new board (so the original isn't affected)
                new_board = copy.deepcopy(board)

                # simulate a move on the game board
                new_board.set_square(square.name, letter)
                #print("-"*(depth+1), letter, square.name)
                #print("-"*(depth+1), letter, square.name)

                # get a value for this move
                score = self.minimax(new_board, depth=depth+1, maximizing=True)

                # keep track of best score
                best_score = min(score, best_score)

            return best_score
