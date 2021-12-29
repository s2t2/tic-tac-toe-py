


import os

from pandas import DataFrame

from app.game import Game
from app.player import set_player

X_STRATEGY = os.getenv("X_STRATEGY", default="RANDOM")
O_STRATEGY = os.getenv("O_STRATEGY", default="RANDOM")

GAME_COUNT = int(os.getenv("GAME_COUNT", default="100_000"))
#BATCH_SIZE = int(os.getenv("BATCH_SIZE", default="1_000")


import time

class Job:
    def __init__(self):
       self.start_at = None
       self.end_at = None

    def start(self):
        self.start_at = time.perf_counter()

    def end(self):
        self.end_at = time.perf_counter()


    @property
    def duration_seconds(self):
        try:
            return self.end_at - self.start_at
        except:
            return None

    @property
    def duration_mins(self):
        try:
            return self.duration_seconds / 60
        except:
            return None


if __name__ == "__main__":

    job = Job()
    job.start()

    #games = []
    records = []
    for counter in range(0, GAME_COUNT):
        game = Game(players=[
            set_player(letter="X", strategy=X_STRATEGY),
            set_player(letter="O", strategy=O_STRATEGY),
        ])

        game.play()

        #print(game.outcome["message"])
        #games.append(game)
        records.append({
            "game_counter": counter+1, # start at 1 instead of 0
            "outcome": game.outcome["reason"],
            "message": game.outcome["message"],
            "winning_letter": game.winning_letter,
            "winning_squares": ",".join(game.winning_square_names or []),
            "move_count": len(game.turn_history),
            #"turn_history": ",".join(game.winning_square_names),
        })

    job.end()
    print("------------------------")
    print("PLAYED", len(records), "GAMES!", f"... (IN {job.duration_seconds} SECONDS)")


    df = DataFrame(records)

    print(df.head())

    print("-----------------")
    print("OUTCOMES:")

    print(df["message"].value_counts(normalize=True))

    print("------------------------")
    print("SAVING DATA TO FILE...")

    csv_filename = f"{game.players[0].letter}_{game.players[0].player_type}_vs_{game.players[1].letter}_{game.players[1].player_type}.csv".lower()
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "..", "data", csv_filename)
    df.to_csv(csv_filepath, index=False)
    print(os.path.abspath(csv_filepath))

    #breakpoint()
