
# Tic Tac Toe (AI/ML)

> NOTE: this is currently a work in progress!

The [computer players](/app/player.py) in the Tic Tac Toe app use a predefined algorithm to select the best move. Let's see if we can train machine learning models to play the game instead.

## Existing Datasets

There is a [dataset of tic-tac-toe endgames](https://archive.ics.uci.edu/ml/datasets/Tic-Tac-Toe+Endgame) from UC Irvine. The inputs are the terminal board states, and the output is the game outcome ("positive" or "negative") for the "X" player. It is possible to [train a nice classifier](/endgames/Endgame_Model_Training.ipynb) on their data. But it represents terminal game states only, whereas an AI agent would need to assess non-terminal game states as well. And it assumes the perspective of the "X" player only, whereas an AI agent would need to be able to play as "O" as well.

## Dataset Generation

So let's generate a dataset of terminal and non-terminal game states, for both players (in case there are strategy differences between "X" going first and "O" going second).

In this step, we generate moves datasets for model training and evaluation. The test/train splits are out of scope for this step, and will be done later, during model training.

The inputs are the board state after the active player makes a move (e.g. "-X-O-X-OX"). The output is the eventual outcome of that move for the given player (win, loss, or tie).

We simulate alternating moves until we reach an outcome (win, lose, tie). After reaching an outcome, we assign the eventual outcome value to all moves that player made leading up until the outcome:
  + all winning player's moves get assigned a positive value (1.0)
  + all losing player's moves get assigned a zero (0.0)
  + all moves resulting in a tie get a neutral score (0.5)

Generating the datasets:

```sh
X_STRATEGY="RANDOM" O_STRATEGY="RANDOM" GAME_COUNT=1000 python -m app.jobs.generate_moves

X_STRATEGY="RANDOM" O_STRATEGY="MINIMAX-AB" GAME_COUNT=1000 python -m app.jobs.generate_moves

X_STRATEGY="MINIMAX-AB" O_STRATEGY="RANDOM" GAME_COUNT=1000 python -m app.jobs.generate_moves

X_STRATEGY="MINIMAX-AB" O_STRATEGY="MINIMAX-AB" GAME_COUNT=1000 python -m app.jobs.generate_moves
```

After generating the datasets, we uploaded the CSV files to GitHub, and used a [notebook](/ml/data_prep/Training_Data_Prep.ipynb) to combine the datasets into a single CSV file ("move_values.csv"), which we also upload to GitHub as well:

Datasets:

  + [random_random_1000.csv](https://github.com/s2t2/tic-tac-toe-py/files/7921041/random_random_1000.csv)
  + [random_minimaxab_1000.csv](https://github.com/s2t2/tic-tac-toe-py/files/7921043/random_minimaxab_1000.csv)
  + [minimaxab_random_1000.csv](https://github.com/s2t2/tic-tac-toe-py/files/7921050/minimaxab_random_1000.csv)
  + [minimaxab_minimaxab_1000.csv](https://github.com/s2t2/tic-tac-toe-py/files/7921045/minimaxab_minimaxab_1000.csv)

Combined Datasets:

  + [move_values.csv](https://github.com/s2t2/tic-tac-toe-py/files/7921159/move_values.csv)
  + [move_values_x.csv](https://github.com/s2t2/tic-tac-toe-py/files/7921160/move_values_x.csv)
  + [move_values_o.csv](https://github.com/s2t2/tic-tac-toe-py/files/7921161/move_values_o.csv)
  + [move_values_normalized.csv](https://github.com/s2t2/tic-tac-toe-py/files/7921162/move_values_normalized.csv)
