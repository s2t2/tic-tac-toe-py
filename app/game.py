
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
    def is_over(self) -> bool:
        return (self.has_winner or self.out_of_squares)

    @property
    def has_winner(self) -> bool:
        return self.board.winning_player_name != None

    @property
    def out_of_squares(self) -> bool:
        return not any(self.board.selectable_squares)

    def play(self):
        while not self.is_over:
            print(self.board)
            while True:
                square_name = input(f"PLAYER {self.active_player} PLEASE SELECT A SQUARE (i.e. 'A1'): ").upper()
                try:
                    self.board.set_square(square_name, self.active_player)
                    break
                except:
                    print(f"OOPS UNRECOGNIZED SQUARE NAME '{square_name}'. PLEASE TRY AGAIN...")
                    next
            self.toggle_active_player()
        print(self.board)
        print(self.outcome())

    def outcome(self):
        winner = self.board.winning_player_name
        if winner:
            message = f"{winner} WINS!"
            reason = "THREE_IN_A_ROW"
        elif not any(self.board.selectable_squares):
            message = "TIE"
            reason = "NO_MORE_SQUARES"
        else:
            message = "IN PROGRESS"
            reason = "IN_PROGRESS"
        return {"message": message, "reason": reason, "winner": winner}



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
