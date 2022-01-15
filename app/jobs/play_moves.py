


import os

from pandas import DataFrame

from app.game import Game
from app.player import select_player
from app.jobs.timer import Timer


# for the strategies, use "RANDOM" for random moves, or "MINIMAX-AB" for expert moves
X_STRATEGY = os.getenv("X_STRATEGY", default="RANDOM")
O_STRATEGY = os.getenv("O_STRATEGY", default="RANDOM")

GAME_COUNT = int(os.getenv("GAME_COUNT", default="100_000"))

if __name__ == "__main__":

    timer = Timer()
    timer.start()

    records = []
    for game_counter in range(0, GAME_COUNT):
        game = Game(players=[
            select_player(letter="X", strategy=X_STRATEGY),
            select_player(letter="O", strategy=O_STRATEGY),
        ])

        game.play()

        breakpoint()

        outcome = game.outcome

        # PLAYBACK

        moves = []
        for move_counter, move in enumerate(game.turn_history):
            #print(game.outcome["message"])

            breakpoint()

            active_player = "X" # TODO get from the move
            active_player_outcome = "X_WINS" # TODO: function of the outcome
            active_player_move_value = 1 # TODO: function of the outcome and the active player

            records.append({
                "game_id": game_counter+1, # start at 1 instead of 0
                "move_id": move_counter+1,
                "board_state": "TODO",
                "active_player": active_player,
                "move": "A1",
                # playback allows us to know the eventual outcome of the move for the active player
                "move_value": active_player_move_value,
            })

    timer.end()
    print("------------------------")
    print("PLAYED", GAME_COUNT, "GAMES!", f"... (IN {timer.duration_seconds} SECONDS)")
    print("GENERATED", len(records), "MOVES")

    df = DataFrame(records)

    print(df.head())

    print("-----------------")
    print("MOVE VALUES:")

    print(df["move_value"].value_counts(normalize=True))

    print("------------------------")
    print("SAVING DATA TO FILE...")

    csv_filename = f"{game.players[0].letter}_{game.players[0].player_type}"
    csv_filename += "_vs_"
    csv_filename += f"{game.players[1].letter}_{game.players[1].player_type}"
    csv_filename += f"{GAME_COUNT}.csv"
    csv_filename = csv_filename.lower()
    csv_filepath = os.path.join(os.path.dirname(__file__), "..", "..", "data", "moves", csv_filename)
    df.to_csv(csv_filepath, index=False)
    print(os.path.abspath(csv_filepath))

    #breakpoint()
