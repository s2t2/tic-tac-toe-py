
import copy
from math import inf

from .minimax import MinimaxPlayer, OPPOSITE_LETTER

class MinimaxABPlayer(MinimaxPlayer):
    """
    A faster version of the Minimax Computer Player.

    Implements "alpha-beta pruning" to prevent unnecessary game state simulations.
    """
    # https://www.javatpoint.com/ai-alpha-beta-pruning
    # https://stackabuse.com/minimax-and-alpha-beta-pruning-in-python/
    # https://github.com/KruZZy/tic-tac-toe/blob/master/ai.py

    def __init__(self, letter, name=None, player_type=None):
        player_type = player_type or "MINIMAX-AB"
        super().__init__(name=name, letter=letter, player_type=player_type)


    def minimax(self, board, depth=0, maximizing=True, alpha=None, beta=None):
        """
        Evaluates a given board state from the perspective of the given player (maximizing or not).

        Returns a score for terminal board states, where positive values correspond with desirable outcomes.

        Otherwise checks all possible next moves recursively until an end state is reached.

        When simulating future game states, it flips control to the next player and assumes they will follow the same strategy.

        Implements "alpha beta pruning", which prevents unnecessary searches of the tree.

            Given a node with two children, each with their own children (i.e. the "grandchildren"),
            after evaluating the values of the first child and both its grandchildren,
            and evaluating the first grandchild of the second child:
            if the first grandchild's value is better than the first child (and both its grandchildren),
            then there's no need to evaluate the final grandchild, because we already know we're going with the second child.

            alpha is the best already explored move for the maximizing player (initial value -inf)

            beta is the best already explored move for the minimizing player (initial value inf)

        Developer Notes:

            + Consider changing the maximizing param from a bool to a str representing the active player's letter.

            + Consider initializing the depth as the board's current move count (length of its move history) - once implemented.
        """

        # use previous alpha and beta values, if available (so we can remember the best previously explored options)
        alpha = alpha or -inf # best prev value for maximizing player
        beta = beta or inf # best prev value for minimizing player

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
                score = self.minimax(new_board, depth=depth+1, maximizing=False, alpha=alpha, beta=beta) # increment depth, flip to next player

                # keep track of best score
                best_score = max(score, best_score)

                # alpha-beta pruning
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break

            return best_score #, alpha, beta

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
                score = self.minimax(new_board, depth=depth+1, maximizing=True, alpha=alpha, beta=beta) # increment depth, flip to next player

                # keep track of best score
                best_score = min(score, best_score)

                # alpha-beta pruning
                beta = min(beta, best_score)
                if beta <= alpha:
                    break

            return best_score #, alpha, beta
