
# todo: test


from app.player import ComputerPlayer, MinimaxPlayer
from app.board import Board
#from app.game import Game

def test_computer_player():

    # RANDOM STRATEGY

    player = ComputerPlayer(name="Randy", letter="X", strategy="RANDOM")

    board = Board()
    assert len(board.selectable_squares) == 9

    selected_square = player.select_square(board)
    assert selected_square in [square.name for square in board.selectable_squares]



def test_minimax_player_x():


    player = MinimaxPlayer(letter="X")
    board = Board()
    board.set_square("A1", "X")
    board.set_square("A2", "O")
    board.set_square("B1", "X")
    board.set_square("B2", "O")
    selected_square = player.select_square(board)
    assert selected_square.name == "C1"

def test_minimax_player_o():

    player = MinimaxPlayer(letter="O")
    board = Board()
    board.set_square("A2", "O")
    board.set_square("A1", "X")
    board.set_square("B2", "O")
    board.set_square("B1", "X")
    selected_square = player.select_square(board)
    assert selected_square.name == "C2"




def test_minimax_player_blocks():

    player = MinimaxPlayer(letter="X")
    board = Board()
    board.set_square("A1", "X")
    board.set_square("B1", "O")
    board.set_square("B2", "X")
    selected_square = player.select_square(board)
    assert selected_square.name == "C3"

    #player = MinimaxPlayer(name="Minnie", letter="O")
    #board = Board()
    #board.set_square("A1", "X")
    #board.set_square("B1", "O")
    #board.set_square("B2", "X")
    #selected_square = player.select_square(board)
    #assert selected_square.name == "C3"
