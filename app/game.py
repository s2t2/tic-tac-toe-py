
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

        self.players = ["X", "O"]
        self.players_cycle = cycle(self.players) # BE CAREFUL OF INFINITE LOOPS
        self.active_player = None
        self.toggle_active_player() # set X as the first player

        self.result = None

        # load from pre-saved state
        self.turn_history = turn_history or []
        if any(self.turn_history):
            for player_name, square_name in self.turn_history:
                self.board.set_square(square_name, player_name)
                self.toggle_active_player()


    #def take_turn(self, player_name, square_name):
    #    self.board.set_square(player_name, square_name)
    #    self.toggle_active_player()


    def toggle_active_player(self):
        self.active_player = next(self.players_cycle) # https://stackoverflow.com/questions/5237611/itertools-cycle-next

    def play(self):
        while not self.result:
            print(self.board)

            # SQUARE SELECTION

            while True:
                square_name = input(f"PLAYER {self.active_player} PLEASE SELECT A SQUARE (i.e. 'A1'): ").upper()
                try:
                    self.board.set_square(square_name, self.active_player)
                    break
                except:
                    print(f"OOPS UNRECOGNIZED SQUARE NAME '{square_name}'. PLEASE TRY AGAIN...")
                    next
            self.toggle_active_player()

            # DON'T REPEAT THE PROCESS IF ANY OF THESE CONDITIONS ARE MET...

            if self.board.winning_player_name:
                self.result = f"{self.board.winning_player_name} WINS!"

            #print("SELECTABLE:", self.board.selectable_squares)
            if not any(self.board.selectable_squares):
                self.result = "TIE"

        print(self.board)
        print("---------------------")
        print("RESULT:", self.result)
        print("THANKS FOR PLAYING!")

    #def take_turn(self, square_name):
    #    self.board.set_square(square_name, self.active_player_name)
    #    self.toggle_active_player()



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
        game.winning_player
