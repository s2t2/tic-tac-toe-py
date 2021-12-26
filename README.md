

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

Play a game:

```sh
python -m app.game
```

Simulate many games:

```sh
python -m app.jobs.simulate
```

X_STRATEGY="RANDOM" O_STRATEGY="RANDOM" GAME_COUNT=100000 python -m app.jobs.simulate
```


## Testing

```sh
pytest
```
