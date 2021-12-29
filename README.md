

# Tic Tac Toe

An adversarial game.

[![Maintainability](https://api.codeclimate.com/v1/badges/23f08f09e8f419f21df0/maintainability)](https://codeclimate.com/github/s2t2/tic-tac-toe-py/maintainability)


![Tests](https://github.com/s2t2/tic-tac-toe-py/actions/workflows/python-app.yml/badge.svg)

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


X_STRATEGY="RANDOM" O_STRATEGY="RANDOM" GAME_COUNT=100 python -m app.jobs.play_games
X_STRATEGY="MINIMAX" O_STRATEGY="MINIMAX" GAME_COUNT=100 python -m app.jobs.play_games

X_STRATEGY="RANDOM" O_STRATEGY="MINIMAX" GAME_COUNT=100 python -m app.jobs.play_games
X_STRATEGY="RANDOM" O_STRATEGY="MINIMAX-AB" GAME_COUNT=100 python -m app.jobs.play_games
```



## Testing

```sh
pytest
```
