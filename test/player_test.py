


import pytest

from app.player import ComputerPlayer, MinimaxPlayer, MinimaxABPlayer, select_player, HumanPlayer, PlayerSelectionError
from app.board import Board
#from app.game import Game



#
# PLAYER SELECTION
#

def test_player_selection():

    # HUMAN PLAYER

    player = select_player(letter="X", strategy="HUMAN")
    assert isinstance(player, HumanPlayer)
    assert player.letter == "X"

    # RANDOM COMPUTER PLAYER

    for strategy in ["COMPUTER", "RANDOM", "COMPUTER-EASY"]:
        player = select_player(letter="X", strategy=strategy)
        assert isinstance(player, ComputerPlayer)
        assert player.letter == "X"

    # HARD COMPUTER PLAYER

    for strategy in ["MINIMAX", "COMPUTER-HARD"]:
        player = select_player(letter="X", strategy=strategy)
        assert isinstance(player, MinimaxPlayer)
        assert player.letter == "X"

    # FASTER HARD COMPUTER PLAYER

    player = select_player(letter="X", strategy="MINIMAX-AB")
    assert isinstance(player, MinimaxABPlayer)
    assert player.letter == "X"

    # OOPS

    with pytest.raises(PlayerSelectionError) as err:
        # we expect this code will raise an error
        select_player(letter="X", strategy="OOPS")


#
# RANDOM COMPUTER PLAYER
#

def test_computer_player():

    # RANDOM STRATEGY

    player = ComputerPlayer(name="Randy", letter="X") # strategy="RANDOM"

    board = Board()
    assert len(board.selectable_squares) == 9

    selected_square = player.select_square(board)
    assert selected_square in [square.name for square in board.selectable_squares]



#
# MINIMAX COMPUTER PLAYER
#
# ... we want to test both types of minimax player the same way (their only difference is speed)
#

def setup_minimax_players(letter):
    return [
        MinimaxPlayer(letter=letter),
        MinimaxABPlayer(letter=letter),
    ]

def test_minimax_player_x():

    for player in setup_minimax_players("X"):

        board = Board()
        board.set_square("A1", "X")
        board.set_square("A2", "O")
        board.set_square("B1", "X")
        board.set_square("B2", "O")
        assert player.select_square(board) == "C1"


def test_minimax_player_o():

    for player in setup_minimax_players("O"):

        board = Board()
        board.set_square("A2", "O")
        board.set_square("A1", "X")
        board.set_square("B2", "O")
        board.set_square("B1", "X")
        assert player.select_square(board) == "C2"


def test_minimax_player_blocks():

    for player in setup_minimax_players("O"):

        board = Board()
        board.set_square("A1", "X")
        board.set_square("B1", "O")
        board.set_square("B2", "X")
        assert player.select_square(board) == "C3"


def test_minimax_player_o_blocks():

    for player in setup_minimax_players("O"):

        board = Board()
        board.set_square("A1", "X")
        board.set_square("C1", "O")
        board.set_square("B2", "X")
        assert player.select_square(board) == "C3"


def test_minimax_more():

    for player in setup_minimax_players("O"):

        board = Board()
        board.set_square("C2", "O")
        board.set_square("B1", "X")
        board.set_square("A2", "O")
        board.set_square("B2", "X")
        assert player.select_square(board) == "B3"

        board.set_square("B3", "0")
        board.set_square("A3", "X")
        assert player.select_square(board) == "C1"


def test_minimax_terminal():

    for player in setup_minimax_players("O"):

        board = Board()
        board.set_square("A1", "X")
        board.set_square("B2", "O")
        board.set_square("C1", "X")
        assert player.select_square(board) == "B1" # for good measure

        board.set_square("B1", "O")
        board.set_square("B3", "X")
        board.set_square("A2", "O")
        board.set_square("C2", "X")
        assert player.select_square(board) == "C3" # an immediately terminal condition
