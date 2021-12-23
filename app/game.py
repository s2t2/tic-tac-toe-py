
from itertools import cycle

from app.board import Board
#from app.outcome import Outcome #, WIN_REASON, TIE_REASON

WIN_REASON = "THREE_IN_A_ROW"
TIE_REASON = "NO_MORE_SQUARES"

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

class Game:
    def __init__(self, turn_history=None):
        """Params

            turn_history (list) : saved game state like [
                ("X", "A1"),
                ("O", "C2"),
                ("X", "B1"),
                ("O", "B2"),
                ("X", "C1"),
            ]

        """
        self.board = Board()
        #self.outcome = self.board.outcome

        self.players = ["X", "O"]
        self.players_cycle = cycle(self.players) # BE CAREFUL OF INFINITE LOOPS
        self.active_player = None
        self.toggle_active_player() # set X as the first player

        # load from pre-saved state
        self.turn_history = [] # instead of setting directly, simulate gamplay through the turn taking mechanism
        if turn_history:
            self.take_turns(turn_history)

    def toggle_active_player(self):
        self.active_player = next(self.players_cycle) # https://stackoverflow.com/questions/5237611/itertools-cycle-next

    def take_turn(self, turn: tuple):
        """
        This is a high-level interface that increments the turn history.
        Pass the turn param as a tuple in the form of (player_name, square_name).
        """
        player_name, square_name = turn
        self.board.set_square(square_name, player_name)
        self.turn_history.append(turn)
        self.toggle_active_player()

    def take_turns(self, turns: list):
        """
        This is a high-level interface that increments the turn history.
        Pass the turns param as a list of tuples in the form of (player_name, square_name).
        """
        for turn in turns:
            self.take_turn(turn)

    def play(self):
        """Play a Human vs Human game!"""
        while not self.outcome:
            print(self.board)
            while True:
                # human turn
                square_name = input(f"PLAYER {self.active_player} PLEASE SELECT A SQUARE (i.e. 'A1'): ").upper()
                try:
                    turn = (self.active_player, square_name)
                    self.take_turn(turn)
                    break # break out of the input loop to conclude the turn and go to the next player
                except:
                    print(f"OOPS UNRECOGNIZED SQUARE NAME '{square_name}'. PLEASE TRY AGAIN...")
                    next # ask the user for another input
        print(self.board)
        print(self.outcome)

    @property
    def winner(self):
        """
        Checks to see if any win conditions have been met, and if so by which player.
        """
        for square_names in WINNING_COMBINATIONS:
            squares = self.board.get_squares(square_names)
            player_names = [square.player_name for square in squares] #> ['X', None, None]
            # if the same player controls all three squares:
            if len(player_names) == 3 and len(list(set(player_names))) == 1:
                winning_player = player_names[0]
                if winning_player:
                    return {"player_name": winning_player, "square_names": square_names}
        return None

    #@property
    #def winning_player_name(self):
    #    try:
    #        return self.winner["player_name"]
    #    except:
    #        return None

    #@property
    #def winning_square_names(self):
    #    try:
    #        return self.winner["square_names"]
    #    except:
    #        return None

    @property
    def outcome(self):
        """
        Checks if game is over due to various conditions.

        Returns an outcome object if the game has ended, otherwise None if game is still in progress.
        """
        winner = self.winner
        if winner:
            #return Outcome(winner=winner, reason=WIN_REASON)
            return {
                "reason": WIN_REASON,
                "message": f"{winner['player_name']} WINS!",
                "winner": winner
            }
        elif self.board.out_of_squares:
            #return Outcome(winner=None, reason=TIE_REASON)
            return {
                "reason": TIE_REASON,
                "message": "TIE GAME",
                "winner": None
            }
        else:
            return None

    #@property
    #def status(self):
    #    try:
    #        return self.outcome.reason
    #    except:
    #        return "IN_PROGRESS"







if __name__ == "__main__":

    from app import APP_ENV

    if APP_ENV == "development":

        preload = input("Would you like to use a pre-saved game state? (Y/N): ")
        if preload.upper() == "Y":

            game = Game(turn_history=[
                ("X", "A1"),
                ("O", "A2"),
                ("X", "B1"),
                ("O", "B2"),
            ])
            game.play()

        else:

            game = Game()
            game.play()

    else:

        game = Game(turn_history=[
            ("X", "A1"),
            ("O", "A2"),
            ("X", "B1"),
            ("O", "B2"),
            ("X", "C1"),
        ])
        print(game.outcome)
