
# Tic Tac Toe (AI)

The [computer players](/app/player.py) in the Tic Tac Toe app use a predefined algorithm to select the best move. Let's see if we can train machine learning models to play the game instead.

## Moves Dataset

Generates moves dataset for model training and evaluation (the test/train splits are out of scope for this step, and will be done later). The inputs for each move are the board state and the active player (i.e. "X" or "O"). The output is the player's selected move (i.e. which square they chose). We simulate alternating moves until we reach an outcome (win, lose, tie). After reaching an outcome, we can assign the eventual outcome value to all moves that player made leading up until the outcome:
  + all winning player's moves get assigned a positive value (+1)
  + all losing player's moves get assigned a negative value (-1)
  + all moves resulting in a tie get a neutral score (0)

Exports a CSV file in the "data" directory (e.g "/data/moves/x_random_vs_o_random_10000.csv").

Generating the datasets:

```sh
GAME_COUNT=3 X_STRATEGY="RANDOM" O_STRATEGY="RANDOM" python -m app.jobs.play_moves
```
