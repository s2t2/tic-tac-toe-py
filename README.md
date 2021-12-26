

# Tic Tac Toe

An adversarial game.

## Setup

```sh
conda create -n tictactoe-env python=3.8
```

```sh
conda activate tictactoe-env
```

```sh
pip install -r requirements.txt
```

## Usage

Play a game (human vs human, human vs computer, computer vs computer):

```sh
python -m app.game
```

Play many games (computer vs computer), saves results to CSV file in "data" directory:

```sh
python -m app.jobs.play_games
```

X_STRATEGY="RANDOM" O_STRATEGY="RANDOM" GAME_COUNT=100 python -m app.jobs.play_games
X_STRATEGY="RANDOM" O_STRATEGY="MINIMAX" GAME_COUNT=100 python -m app.jobs.play_games
X_STRATEGY="MINIMAX" O_STRATEGY="MINIMAX" GAME_COUNT=100 python -m app.jobs.play_games
```



## Testing

```sh
pytest
```
