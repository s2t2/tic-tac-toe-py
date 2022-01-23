
# Tic Tac Toe (AI/ML)

> NOTE: this is currently a work in progress!

The [computer players](/app/player.py) in the Tic Tac Toe app use a predefined algorithm to select the best move. Let's see if we can train machine learning models to play the game instead.

## Data Prep

Generates moves dataset for model training and evaluation. The test/train splits are out of scope for this step, and will be done later, during model training.

The inputs are the board state after the active player makes a move (e.g. "-X-O-X-OX"). The output is the eventual outcome of that move for the given player (win, loss, or tie).

We simulate alternating moves until we reach an outcome (win, lose, tie). After reaching an outcome, we can assign the eventual outcome value to all moves that player made leading up until the outcome:
  + all winning player's moves get assigned a positive value (1.0)
  + all losing player's moves get assigned a zero (0.0)
  + all moves resulting in a tie get a neutral score (0.5)

Generating the datasets:

```sh
X_STRATEGY="RANDOM" O_STRATEGY="RANDOM" GAME_COUNT=1000 python -m app.jobs.play_moves

X_STRATEGY="RANDOM" O_STRATEGY="MINIMAX-AB" GAME_COUNT=1000 python -m app.jobs.play_moves

X_STRATEGY="MINIMAX-AB" O_STRATEGY="RANDOM" GAME_COUNT=1000 python -m app.jobs.play_moves

X_STRATEGY="MINIMAX-AB" O_STRATEGY="MINIMAX-AB" GAME_COUNT=1000 python -m app.jobs.play_moves
```

After generating the datasets, we uploaded the CSV files to GitHub, and used a [notebook](/ml/data_prep/Training_Data_Prep.ipynb) to combine the datasets into a single CSV file ("move_values.csv"), which we also upload to GitHub as well:

  + [random_random_1000.csv](https://github.com/s2t2/tic-tac-toe-py/files/7920779/random_random_1000.csv)
  + [random_minimaxab_1000.csv](https://github.com/s2t2/tic-tac-toe-py/files/7920780/random_minimaxab_1000.csv)
  + [minimaxab_random_1000.csv](https://github.com/s2t2/tic-tac-toe-py/files/7920850/minimaxab_random_1000.csv)
  + [minimaxab_minimaxab_1000.csv](https://github.com/s2t2/tic-tac-toe-py/files/7920782/minimaxab_minimaxab_1000.csv)
  + [move_values.csv](https://github.com/s2t2/tic-tac-toe-py/files/7920856/move_values.1.csv)
