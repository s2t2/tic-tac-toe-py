
# Tic Tac Toe (AI)

> NOTE: this is currently a work in progress!

The [computer players](/app/player.py) in the Tic Tac Toe app use a predefined algorithm to select the best move. Let's see if we can train machine learning models to play the game instead.

## Generating Moves Data

Generates moves dataset for model training and evaluation. The test/train splits are out of scope for this step, and will be done later, during model training.

The inputs for each move are the board state (e.g. "-X-O-X-OX" and the active player (i.e. "X" or "O"). The output is the player's selected move, represented by the selected square's index position in the board notation string (0-8).

We simulate alternating moves until we reach an outcome (win, lose, tie). After reaching an outcome, we can assign the eventual outcome value to all moves that player made leading up until the outcome:
  + all winning player's moves get assigned a positive value (+1)
  + all losing player's moves get assigned a negative value (-1)
  + all moves resulting in a tie get a neutral score (0)

Generating the datasets:

```sh
GAME_COUNT=100000 X_STRATEGY="RANDOM" O_STRATEGY="RANDOM" python -m app.jobs.play_moves
```

Exports a CSV file in the "data" directory (e.g "/data/moves/x_random_vs_o_random_10000.csv"). Example results:

|game_id|move_id|board_state|player|square_idx|reward|
|-------|-------|-----------|------|---------|------|
|1      |1      | `---------` |`X`    |5       | 0   |
|1      |2      | `-----X---` |`O`    |7       | 0   |
|1      |3      | `-----X-O-` |`X`    |8       | 0   |
|1      |4      | `-----X-OX` |`O`    |3       | 0   |
|1      |5      | `---O-X-OX` |`X`    |1       | 0   |
|1      |6      | `-X-O-X-OX` |`O`    |2       | 0   |
|1      |7      | `-XOO-X-OX` |`X`    |6       | 0   |
|1      |8      | `-XOO-XXOX` |`O`    |4       | 0   |
|1      |9      | `-XOOOXXOX` |`X`    |0       | 0   |
|2      |1      |`---------`  |`X`    |1       |1    |
|2      |2      |`-X-------`  |`O`    |8       |-1   |
|2      |3      |`-X------O`  |`X`    |0       |1    |
|2      |4      |`XX------O`  |`O`    |4       |-1   |
|2      |5      |`XX--O---O`  |`X`    |2       |1    |
|3      |1      |`---------`  |`X`    |4       |-1   |
|3      |2      |`----X----`  |`O`    |7       |1    |
|3      |3      |`----X--O-`  |`X`    |2       |-1   |
|3      |4      |`--X-X--O-`  |`O`    |8       |1    |
|3      |5      |`--X-X--OO`  |`X`    |5       |-1   |
|3      |6      |`--X-XX-OO`  |`O`    |6       |1    |

## Model Selection and Evaluation

TBD

## Model Training

TBD
