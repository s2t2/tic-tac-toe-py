
from itertools import cycle

from app.board import Board

class Game:
    def __init__(self, turn_history=None):
        self.players = ["X", "O"]
        self.players_cycle = cycle(self.players) # BE CAREFUL OF INFINITE LOOPS
        self.board = Board()
        self.active_player = None
        self.turn_history = turn_history or []
        self.result = None

    def toggle_active_player(self):
        self.active_player = next(self.players_cycle) # https://stackoverflow.com/questions/5237611/itertools-cycle-next

    def play(self):
        while not self.result:

            # BEGINNING OF TURN (PLAYER ALTERNATION)

            self.toggle_active_player()
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


if __name__ == "__main__":

    game = Game()
    game.play()

    #game = Game(turn_history=[
    #    ("X", "A1"),
    #    ("O", "C2"),
    #    ("X", "B1"),
    #    ("O", "B2"),
    #    ("X", "C1"),
    #])
    #print(game.board)
    #print("RESULT:", game.result)
