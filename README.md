

# Tic Tac Toe

An adversarial game.

[![Maintainability](https://api.codeclimate.com/v1/badges/23f08f09e8f419f21df0/maintainability)](https://codeclimate.com/github/s2t2/tic-tac-toe-py/maintainability)

![Tests](https://github.com/s2t2/tic-tac-toe-py/actions/workflows/python-app.yml/badge.svg)

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Setup

Optionally fork this [remote repository](https://github.com/s2t2/tic-tac-toe-py), to create a copy under your own control.

Then "clone" or download the remote repository (or your forked copy) onto your local computer, for example to your Desktop. Then navigate to wherever you downloaded the repo:

```sh
cd ~/Desktop/tic-tac-toe-py
```

> NOTE: all subsequent commands assume you will be running them from the local repo's root directory

Create a virtual environment (first time only):

```sh
conda create -n tictactoe-env python=3.8
```

Activate the virtual environment (first time, and any subsequent times you want to play):

```sh
conda activate tictactoe-env
```

Install package dependencies within the virtual environment (first time only):

```sh
pip install -r requirements.txt
```

> FYI: see the ["requirements.txt"](/requirements.txt) file for a list of packages that will be installed

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the "requirements.txt" file exists (see the initial `cd` step above).


## Player Types

When you play games, you'll be able to select any of the following combinations of players:

player type(s) | description
--- | ---
`HUMAN` | A human player who will input their selections.
`COMPUTER-EASY` or `RANDOM` | A computer player which makes random selections. Easy to beat.
`COMPUTER-HARD` or `MINIMAX` | A computer player which thinks ahead to make optimal selections. Uses the "minimax" algorithm to simulate moves and evaluate all possible game states. Impossible to beat.
`MINIMAX-AB` | A much faster version of the hard computer player. Uses "alpha-beta" pruning to skip evaluations of unnecessary game states.

## Usage

### Game Play

Play a game (human vs human, human vs computer, computer vs computer):

```sh
python -m app.game
```


### Game Simulation

Play many games (computer vs computer), saves results to CSV file in "data" directory:

```sh
python -m app.jobs.play_games

# optionally pass the player strategies as environment variables:
X_STRATEGY="COMPUTER-HARD" O_STRATEGY="COMPUTER-EASY" GAME_COUNT=100 python -m app.jobs.play_games
```

> NOTE: if you see an error like "ModuleNotFoundError: No module named '...'", it's because the given package isn't installed, so run the `pip` command above to ensure that package has been installed into the virtual environment.


## Testing

Run automated tests, to know whether the app is working as expected:

```sh
pytest
```


## Demo

Here is a demonstration of gameplay between computer players:

```
SELECT X PLAYER TYPE ('HUMAN' / 'COMPUTER-EASY' / 'COMPUTER-HARD'): COMPUTER-HARD
SELECT O PLAYER TYPE ('HUMAN' / 'COMPUTER-EASY' / 'COMPUTER-HARD'): COMPUTER-HARD
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
