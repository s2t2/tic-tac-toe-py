
from itertools import cycle

from app.board import Board

# if a single player has any of these combination of squares, they win:
#WINNING_COMBINATIONS = [
#    [0,1,2], # Row 1
#    [3,4,5], # Row 2
#    [6,7,8], # Row 3
#    [1,4,7], # Column A
#    [2,5,8], # Column B
#    [3,6,9], # Column C
#    [1,5,9], # Diagonal ASC
#    [3,5,7], # Diagonal DESC
#]

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
                #self.result = self.active_player
                self.result = f"{self.board.winning_player_name} WINS!"

            #print("SELECTABLE:", self.board.selectable_squares)
            if not any(self.board.selectable_squares):
                self.result = "TIE"

        print("THANKS FOR PLAYING!")
        print("RESULT:", self.result)


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
