

# Tic Tac Toe

An adversarial game.


[![Maintainability](https://api.codeclimate.com/v1/badges/23f08f09e8f419f21df0/maintainability)](https://codeclimate.com/github/s2t2/tic-tac-toe-py/maintainability)

![Tests](https://github.com/s2t2/tic-tac-toe-py/actions/workflows/python-app.yml/badge.svg)


## Demo

```
(tictactoe-env)  --->> python -m app.game
SELECT X PLAYER TYPE ('HUMAN' / 'COMPUTER' / 'MINIMAX' / 'MINIMAX-AB'): MINIMAX
SELECT O PLAYER TYPE ('HUMAN' / 'COMPUTER' / 'MINIMAX' / 'MINIMAX-AB'): MINIMAX
Would you like to use a pre-saved game state? (Y/N): n

                A   B   C

            1     |   |
               -----------
            2     |   |
               -----------
            3     |   |


PLAYER X THINKING...

                A   B   C

            1     |   |
               -----------
            2     |   |
               -----------
            3   X |   |


PLAYER O THINKING...
... <Square A1> -3
... <Square B1> -3
... <Square C1> -3
... <Square A2> -3
... <Square B2> 0
... <Square C2> -3
... <Square B3> -3
... <Square C3> -3

                A   B   C

            1     |   |
               -----------
            2     | O |
               -----------
            3   X |   |


PLAYER X THINKING...
... <Square A1> 0
... <Square B1> 0
... <Square C1> 0
... <Square A2> 0
... <Square C2> 0
... <Square B3> 0
... <Square C3> 0

                A   B   C

            1   X |   |
               -----------
            2     | O |
               -----------
            3   X |   |


PLAYER O THINKING...
... <Square B1> -5
... <Square C1> -5
... <Square A2> 0
... <Square C2> -5
... <Square B3> -5
... <Square C3> -5

                A   B   C

            1   X |   |
               -----------
            2   O | O |
               -----------
            3   X |   |


PLAYER X THINKING...
... <Square B1> -4
... <Square C1> -4
... <Square C2> 0
... <Square B3> -4
... <Square C3> -4

                A   B   C

            1   X |   |
               -----------
            2   O | O | X
               -----------
            3   X |   |


PLAYER O THINKING...
... <Square B1> 0
... <Square C1> 0
... <Square B3> 0
... <Square C3> 0

                A   B   C

            1   X | O |
               -----------
            2   O | O | X
               -----------
            3   X |   |


PLAYER X THINKING...
... <Square C1> -2
... <Square B3> 0
... <Square C3> -2

                A   B   C

            1   X | O |
               -----------
            2   O | O | X
               -----------
            3   X | X |


PLAYER O THINKING...
... <Square C1> -1
... <Square C3> 0

                A   B   C

            1   X | O |
               -----------
            2   O | O | X
               -----------
            3   X | X | O


PLAYER X THINKING...
... <Square C1> 0

                A   B   C

            1   X | O | X
               -----------
            2   O | O | X
               -----------
            3   X | X | O


{'winner': None, 'reason': 'NO_MORE_SQUARES', 'message': 'TIE GAME'}
```

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
