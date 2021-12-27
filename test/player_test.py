
# todo: test


from app.player import ComputerPlayer, MinimaxPlayer, MinimaxABPlayer
from app.board import Board
#from app.game import Game

def test_computer_player():

    # RANDOM STRATEGY

    player = ComputerPlayer(name="Randy", letter="X") # strategy="RANDOM"

    board = Board()
    assert len(board.selectable_squares) == 9

    selected_square = player.select_square(board)
    assert selected_square in [square.name for square in board.selectable_squares]



#
# MINIMAX
#

def test_minimax_player_x():

    player = MinimaxPlayer(letter="X")
    board = Board()
    board.set_square("A1", "X")
    board.set_square("A2", "O")
    board.set_square("B1", "X")
    board.set_square("B2", "O")
    assert player.select_square(board) == "C1"

def test_minimax_player_o():

    player = MinimaxPlayer(letter="O")
    board = Board()
    board.set_square("A2", "O")
    board.set_square("A1", "X")
    board.set_square("B2", "O")
    board.set_square("B1", "X")
    assert player.select_square(board) == "C2"

def test_minimax_player_blocks():

    player = MinimaxPlayer(letter="X")
    board = Board()
    board.set_square("A1", "X")
    board.set_square("B1", "O")
    board.set_square("B2", "X")
    assert player.select_square(board) == "C3"

def test_minimax_player_o_blocks():

    player = MinimaxPlayer(letter="O")
    board = Board()
    board.set_square("A1", "X")
    board.set_square("C1", "O")
    board.set_square("B2", "X")
    assert player.select_square(board) == "C3"

def test_minimax_more():

    player = MinimaxPlayer(letter="O")
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

    player = MinimaxPlayer(letter="O")
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












# TODO: refactor this and other minimax tests, for use on both player classes
# ... OR change the computer player interface to use strategies
def test_minimax_ab_terminal():

    player = MinimaxABPlayer(letter="O")
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
