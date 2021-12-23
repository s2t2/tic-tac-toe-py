

#import pytest

#
# TURN HISTORIES / GAME STATES
#

IN_PROGRESS = [
    ("X", "B2"),
    ("O", "A1"),
    ("X", "C1"),
]

TIE_GAME = [
    ("X", "A1"),
    ("O", "B2"),
    ("X", "B1"),
    ("O", "C1"),
    ("X", "A3"),
    ("O", "A2"),
    ("X", "C2"),
    ("X", "B3"),
    ("O", "C3"),
]

X_WINS = [
    ("X", "A1"),
    ("O", "A2"),
    ("X", "B1"),
    ("O", "B2"),
    ("X", "C1"),
]

#
# GAMES
#

#@pytest.fixture(scope="module")
#def tie_game_turns():
#    return ...
