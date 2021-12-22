
from itertools import cycle

from app.board import Board

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



    @property
    def outcome(self):
        return self.board.outcome

    @property
    def winner(self):
        return self.board.winner

    def play(self):
        while not self.outcome:
            print(self.board)
            while True:
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
        game.outcome()
