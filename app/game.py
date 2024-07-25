
from itertools import cycle

from app.board import Board, SquareTakenError
from app.player import select_player
from app.move import Move

class Game:
    def __init__(self, players=None, turn_history=None):
        """Params

            turn_history (list) : saved game state like [
                ("X", "A1"),
                ("O", "C2"),
                ("X", "B1"),
                ("O", "B2"),
                ("X", "C1"),
            ]

            players (list) with letters matching order of turn history, if provided.

        """
        self.board = Board()

        self.players = players or [
            select_player(letter="X", strategy="HUMAN"),
            select_player(letter="O", strategy="HUMAN"),
        ]
        self.players_cycle = cycle(self.players) # BE CAREFUL OF INFINITE LOOPS
        self.active_player = None
        self.toggle_active_player() # set X as the first player

        # load from pre-saved state
        self.turn_history = [] # instead of setting directly, simulate gamplay through the turn taking mechanism
        self.move_history = [] # like the turn history, but stores board states as well (for model training)
        if turn_history:
            self.take_turns(turn_history)


    def toggle_active_player(self):
        self.active_player = next(self.players_cycle) # https://stackoverflow.com/questions/5237611/itertools-cycle-next

    def take_turn(self, turn: tuple):
        """
        This is a high-level interface that increments the turn history.
        Pass the turn param as a tuple in the form of (player_letter, square_name).
        """
        player_letter, square_name = turn
        initial_board_state = self.board.notation # important to note this before changing the board

        move = Move(board_state=initial_board_state, active_player=player_letter, selected_square=square_name)

        # make the move / change the board state:
        self.board.set_square(square_name, player_letter)
        self.turn_history.append(turn)
        self.move_history.append(move)
        self.toggle_active_player()

    def take_turns(self, turns: list):
        """
        This is a high-level interface that increments the turn history.
        Pass the turns param as a list of tuples in the form of (player_letter, square_name).
        """
        for turn in turns:
            self.take_turn(turn)


    @property
    def outcome(self):
        return self.board.outcome

    @property
    def winner(self):
        return self.board.winner

    @property
    def winning_letter(self):
        return self.board.winning_letter

    @property
    def winning_square_names(self):
        return self.board.winning_square_names


    def play(self):
        while not self.outcome:
            print(self.board)
            while True:
                square_name = self.active_player.select_square(self.board)
                try:
                    turn = (self.active_player.letter, square_name)
                    self.take_turn(turn)
                    break # break out of the input loop to conclude the turn and go to the next player
                except SquareTakenError as err:
                    print("...", err)
                    next
                except:
                    print(f"... OOPS UNRECOGNIZED SQUARE NAME '{square_name}'. PLEASE TRY AGAIN...")
                    next # ask the player for another input (this is only applicable for human players)
        print(self.board)
        print(self.outcome)



if __name__ == "__main__":

    # PLAYER SELECTION

    x_strategy = input("SELECT X PLAYER TYPE ('HUMAN' / 'COMPUTER-EASY' / 'COMPUTER-HARD'): ").upper() or "HUMAN"
    o_strategy = input("SELECT O PLAYER TYPE ('HUMAN' / 'COMPUTER-EASY' / 'COMPUTER-HARD'): ").upper() or "COMPUTER-HARD"

    players = [
        select_player(letter="X", strategy=x_strategy),
        select_player(letter="O", strategy=o_strategy),
    ]

    # GAME PLAY

    preload = input("Would you like to use a pre-saved game state? (Y/N): ").upper() or "N"
    if preload.upper() == "Y":

        game = Game(players=players, turn_history=[
            ("X", "A1"),
            ("O", "B1"),
            ("X", "B2"),
        ])
        game.play()

    else:

        game = Game(players=players)
        game.play()
