
from itertools import cycle

from app.board import Board

class Game:
    def __init__(self):
        self.players = ["X", "O"]
        self.players_cycle = cycle(self.players) # BE CAREFUL OF INFINITE LOOPS
        self.active_player = None
        self.winner = None
        self.board = Board()

    def toggle_active_player(self):
        self.active_player = next(self.players_cycle) # https://stackoverflow.com/questions/5237611/itertools-cycle-next

    def main_loop(self):
        while self.winner == None:
            self.toggle_active_player()

            print(self.board)
            selected_square = input(f"PLAYER {self.active_player} PLEASE SELECT A SQUARE (i.e. 'A1'): ")

            #if selected_square == "QUIT":
            #    self.winner == self.active_player

            self.board.set_square(selected_square, self.active_player)

            # todo: evaluate new game state
            # todo: determine if win condition is reached

            # if self.turn_counter >= "QUIT":
            #     self.winner == self.active_player


        #print("WINNER IS ...", self.winner)


if __name__ == "__main__":

    game = Game()

    game.main_loop()
