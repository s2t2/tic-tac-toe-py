


import os

from pandas import DataFrame

from app import OPPOSITE_LETTERS
#from app.board import SQUARE_NAMES
from app.game import Game
from app.player import select_player
from app.jobs.timer import Timer


# for the strategies, use "RANDOM" for random moves, or "MINIMAX-AB" for expert moves
X_STRATEGY = os.getenv("X_STRATEGY", default="RANDOM")
O_STRATEGY = os.getenv("O_STRATEGY", default="RANDOM")

GAME_COUNT = int(os.getenv("GAME_COUNT", default="1_000"))



class EvaluatedGame(Game):
    @property
    def player_rewards(self):
        if self.winner:
            # reward the winner and punish the loser:
            winning_letter = self.winner["letter"]
            losing_letter = OPPOSITE_LETTERS[winning_letter]
            return {winning_letter: 1, losing_letter: -1}
        else:
            # give neutral scores to both players:
            return {"X": 0, "O": 0}


class MoveEvaluator:
    def __init__(self):
        self.timer = Timer()
        self.players = [
            select_player(letter="X", strategy=X_STRATEGY),
            select_player(letter="O", strategy=O_STRATEGY),
        ]
        self.GAME_COUNT = GAME_COUNT
        self.moves_df = None

    def perform(self, export=True):
        self.timer.start()
        records = []
        for game_counter in range(0, self.GAME_COUNT):
            game = EvaluatedGame(players=self.players)
            game.play()

            player_rewards = game.player_rewards
            for move_counter, move in enumerate(game.move_history):
                active_player = move.active_player

                # if the active player takes this move they will get the outcome
                move.board.set_square(square_name=move.selected_square, player_letter=active_player)

                records.append({
                    "game_id": game_counter + 1, # start ids at 1 instead of 0
                    "move_id": move_counter + 1, # start ids at 1 instead of 0
                    #"board_state": move.board.notation,
                    "a1": move.board.get_square("A1").notation,
                    "b1": move.board.get_square("B1").notation,
                    "c1": move.board.get_square("C1").notation,
                    "a2": move.board.get_square("A2").notation,
                    "b2": move.board.get_square("B2").notation,
                    "c2": move.board.get_square("C2").notation,
                    "a3": move.board.get_square("A3").notation,
                    "b3": move.board.get_square("B3").notation,
                    "c3": move.board.get_square("C3").notation,
                    #"player": active_player,
                    #"square_name": move.selected_square,
                    #"square_idx": SQUARE_NAMES.index(move.selected_square), # translate squares to index 0-8 to match board notation (maybe)
                    "outcome": player_rewards[active_player],
                })

        self.timer.end()
        print("------------------------")
        print("PLAYED", self.GAME_COUNT, "GAMES", f"IN {self.timer.duration_seconds} SECONDS")
        print("TOTAL MOVES:", len(records))
        self.moves_df = DataFrame(records)
        print(self.moves_df.head())

        if export:
            print("------------------------")
            print("SAVING DATA TO FILE...")
            #csv_filename = f"{self.players[0].letter}_{self.players[0].player_type.replace('-','')}"
            #csv_filename += "_vs_"
            #csv_filename += f"_{self.players[1].letter}_{self.players[1].player_type.replace('-','')}"

            csv_filename = self.players[0].player_type.replace('-','') + "_"
            csv_filename += self.players[1].player_type.replace('-','')
            csv_filename += f"_{self.GAME_COUNT}.csv"
            csv_filename = csv_filename.lower()
            csv_filepath = os.path.join(os.path.dirname(__file__), "..", "..", "data", "moves", csv_filename)

            self.moves_df.to_csv(csv_filepath, index=False)
            print(os.path.abspath(csv_filepath))

        return self.moves_df




if __name__ == "__main__":



    job = MoveEvaluator()

    job.perform()
