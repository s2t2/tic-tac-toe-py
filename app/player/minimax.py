


import copy
from math import inf

from .computer import ComputerPlayer

OPPOSITE_LETTER = {"X": "O", "O": "X"}

class MinimaxPlayer(ComputerPlayer):
    # https://www.youtube.com/watch?v=J1GoI5WHBto
    # https://www.youtube.com/watch?v=STjW3eH0Cik
    # https://www.youtube.com/watch?v=fT3YWCKvuQE

    def __init__(self, letter, name=None, player_type=None):
        player_type = player_type or "MINIMAX"
        super().__init__(name=name, letter=letter, player_type=player_type)

    def select_square(self, board):
        print("PLAYER", self.letter, "THINKING...")

        if len(board.selectable_squares) == 9:
            return self.select_random_square(board)

        best_square = None
        best_score = -inf
        for square in board.selectable_squares:
            # make a new board (so the original isn't affected)
            new_board = copy.deepcopy(board)

            # simulate a move on the game board
            new_board.set_square(square.name, self.letter)

            # get a value for this move
            score = self.minimax(new_board, depth=0, maximizing=False) # after setting the square ourselves, we allow the opposing player to take the next turn
            print("...", square, score)

            # update best scorer, and keep track of which square is best
            if score > best_score:
                best_score = score
                best_square = square

        return best_square.name


    def minimax(self, board, depth=0, maximizing=True):
        """
        Evaluates a given board state from the perspective of this player.

        Returns a score for terminal board states, where positive values correspond with desirable outcomes.

        Otherwise checks all possible next moves recursively until an end state is reached.

        When simulating future game states, it flips control to the next player and assumes they will follow the same strategy.

        Developer Notes:

            + Consider changing the maximizing param from a bool to a str representing the active player's letter.

            + Consider initializing the depth as the board's current move count (length of its move history) - once implemented.
        """

        #print(board)

        #
        # TERMINAL CONDITIONS
        #

        if board.outcome:
            #print("-"*(depth+1), "OUTCOME:", board.outcome["message"])
            winner = board.winner
            if winner:
                inverse_move_count = (len(board.selectable_squares)+1) # the number of squares remaining
                if winner["letter"] == self.letter:
                    return 1 * inverse_move_count # a positive score, more positive for faster wins
                else:
                    return -1 * inverse_move_count # negative score, more negative for faster losses
            else:
                return 0 # a neutral score for ties

        #
        # NON-TERMINAL CONDITIONS
        #

        if maximizing == True:
            letter = self.letter

            best_score = -inf
            for square in board.selectable_squares:
                # make a new board (so the original isn't affected)
                new_board = copy.deepcopy(board)

                # simulate a move on the game board
                new_board.set_square(square.name, letter)
                #print("-"*(depth+1), letter, square.name)

                # get a value for this move
                score = self.minimax(new_board, depth=depth+1, maximizing=False) # increment depth, flip to next player

                # keep track of best score
                best_score = max(score, best_score)

            return best_score

        else:
            letter = OPPOSITE_LETTER[self.letter]

            best_score = inf
            for square in board.selectable_squares:
                # make a new board (so the original isn't affected)
                new_board = copy.deepcopy(board)

                # simulate a move on the game board
                new_board.set_square(square.name, letter)
                #print("-"*(depth+1), letter, square.name)

                # get a value for this move
                score = self.minimax(new_board, depth=depth+1, maximizing=True) # increment depth, flip to next player

                # keep track of best score
                best_score = min(score, best_score)

            return best_score
