

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

    def __init__(self, letter, name=None):
        super().__init__(name=name, letter=letter, player_type="COMPUTER")

    def select_square(self, board):
        best_square = None
        best_score = -inf
        for square in board.selectable_squares:
            # make a new board (so the original isn't affected)
            new_board = copy.deepcopy(board)

            # simulate a move on the game board
            new_board.set_square(square.name, self.letter)

            # get a value for this move
            score = self.minimax(new_board, maximizing=True)

            # update best scorer, and keep track of which square is best
            if score > best_score:
                best_score = score
                best_square = square

        return best_square






    def minimax(self, board, depth=0, maximizing=True):

        #print(board)

        if board.outcome:
            print("DEPTH", depth, "OUTCOME:", board.outcome["message"])

            if board.winning_letter == self.letter:
                return 100 * depth+1
            elif board.winning_letter != self.letter:
                return -100 * depth+1
            else:
                return 0

        #print("DEPTH", depth, "NO OUTCOME")

        if maximizing == True:
            letter = self.letter
            #print(f"MAXIMIZING ({letter})...")

            best_score = -inf
            for square in board.selectable_squares:
                # make a new board (so the original isn't affected)
                new_board = copy.deepcopy(board)

                # simulate a move on the game board
                new_board.set_square(square.name, letter)

                # get a value for this move
                score = self.minimax(new_board, depth=depth+1, maximizing=False)

                # keep track of best score
                best_score = max(score, best_score)

                print("...", depth, letter, square.name, score)

            return best_score

        else:
            letter = OPPOSITE_LETTER[self.letter]
            #print(f"MINIMIZING ({letter})...", )

            best_score = inf
            for square in board.selectable_squares:
                # make a new board (so the original isn't affected)
                new_board = copy.deepcopy(board)

                # simulate a move on the game board
                new_board.set_square(square.name, letter)

                # get a value for this move
                score = self.minimax(new_board, depth=depth+1, maximizing=True)

                # keep track of best score
                best_score = min(score, best_score)

                print("...", depth, letter, square.name, score)

            return best_score
