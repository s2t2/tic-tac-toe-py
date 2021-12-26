


#import pytest

#
# TURN HISTORIES / GAME STATES
#

IN_PROGRESS_TURNS = [
    ("X", "B2"),
    ("O", "A1"),
    ("X", "C1"),
]

TIE_GAME_TURNS = [
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

X_WINS_TURNS = [
    ("X", "A1"),
    ("O", "A2"),
    ("X", "B1"),
    ("O", "B2"),
    ("X", "C1"),
]

#
# OUTCOMES
#

TIE_GAME_OUTCOME = {'message': 'TIE GAME', 'reason': 'NO_MORE_SQUARES', 'winner': None}
X_WINS_OUTCOME = {'message': 'X WINS!', 'reason': 'THREE_IN_A_ROW', 'winner': {
    'letter': 'X', 'square_names': ['A1', 'B1', 'C1']}
}


#
# GAMES
#

#@pytest.fixture(scope="module")
#def tie_game_turns():
#    return ...
