
from itertools import cycle

from app.board import Board
from app.player import HumanPlayer, ComputerPlayer

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

        """
        self.board = Board()

        self.players = players or [HumanPlayer("X"), HumanPlayer("O")]
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
        Pass the turn param as a tuple in the form of (player_letter, square_name).
        """
        player_letter, square_name = turn
        self.board.set_square(square_name, player_letter)
        self.turn_history.append(turn)
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
                except:
                    print(f"OOPS UNRECOGNIZED SQUARE NAME '{square_name}'. PLEASE TRY AGAIN...")
                    next # ask the player for another input (this is only applicable for human players)
        print(self.board)
        print(self.outcome)







if __name__ == "__main__":

    from app import APP_ENV

    if APP_ENV == "development":

        # PLAYER SELECTION

        x_player_type = input("SELECT X PLAYER TYPE ('HUMAN' / 'COMPUTER'): ") or "HUMAN"
        o_player_type = input("SELECT O PLAYER TYPE ('HUMAN' / 'COMPUTER'): ") or "HUMAN"

        if x_player_type == "HUMAN":        x_player = HumanPlayer("X")
        elif x_player_type == "COMPUTER":   x_player = ComputerPlayer("X")

        if o_player_type == "HUMAN":        o_player = HumanPlayer("O")
        elif o_player_type == "COMPUTER":   o_player = ComputerPlayer("O")

        players = [x_player, o_player]

        # PRELOAD SELECTION

        preload = input("Would you like to use a pre-saved game state? (Y/N): ")
        if preload.upper() == "Y":

            game = Game(players=players, turn_history=[
                ("X", "A1"),
                ("O", "A2"),
                ("X", "B1"),
                ("O", "B2"),
            ])
            game.play()

        else:

            game = Game(players=players)
            game.play()

    else:

        # PRELOAD FROM SAVED STATE

        #game = Game(turn_history=[
        #    ("X", "A1"),
        #    ("O", "A2"),
        #    ("X", "B1"),
        #    ("O", "B2"),
        #    ("X", "C1"),
        #])
        #print(game.outcome)

        #print("---------------")


        # SIMULATE GAMEPLAY

        game = Game(players=[
            ComputerPlayer("X", strategy="RANDOM"),
            ComputerPlayer("O", strategy="RANDOM")
        ])
        game.play()
