
# todo: test


from app.player import ComputerPlayer
from app.board import Board
#from app.game import Game

def test_computer_player():

    # RANDOM STRATEGY

    player = ComputerPlayer(name="Randy", letter="X", strategy="RANDOM")

    board = Board()
    assert len(board.selectable_squares) == 9

    selected_square = player.select_square(board)
    assert selected_square in [square.name for square in board.selectable_squares]
