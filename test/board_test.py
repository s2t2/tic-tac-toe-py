

from app.board import Board
from app.square import Square

from conftest import X_WINS_OUTCOME

def test_board():
    board = Board()

    assert isinstance(board.get_square("A1"), Square)

    for square in board.get_squares(["A1", "A1", "A3"]):
        assert isinstance(square, Square)


def test_square_selection():
    board = Board()

    assert sorted([square.name for square in board.selectable_squares]) == [
        "A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"
    ]

    board.set_square("A1", "X")

    assert sorted([square.name for square in board.selectable_squares]) == [
        "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"
    ]


def test_winner_determination():
    board = Board()
    assert board.winner == None
    assert board.outcome == None

    board.set_square("A1", "X")
    assert board.winner == None
    assert board.outcome == None

    board.set_square("A2", "O")
    assert board.winner == None
    assert board.outcome == None

    board.set_square("B1", "X")
    assert board.winner == None
    assert board.outcome == None

    board.set_square("B2", "O")
    assert board.winner == None
    assert board.outcome == None

    board.set_square("C1", "X")
    assert board.winner == X_WINS_OUTCOME["winner"]
    assert board.outcome == X_WINS_OUTCOME



def test_board_state_notation():

    board = Board()
    assert board.notation == "---------"

    board.set_square("A1", "X")
    assert board.notation ==  "X--------"

    board.set_square("A2", "O")
    assert board.notation ==  "X--O-----"

    board.set_square("B1", "X")
    assert board.notation ==  "XX-O-----"

    board.set_square("B2", "O")
    assert board.notation ==  "XX-OO----"
