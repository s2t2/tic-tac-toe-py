
from app.game import Game


def test_toggle_active_player():
    game = Game()
    #assert game.active_player == None

    #game.toggle_active_player()
    assert game.active_player == "X"

    game.toggle_active_player()
    assert game.active_player == "O"

    game.toggle_active_player()
    assert game.active_player == "X"

    game.toggle_active_player()
    assert game.active_player == "O"


def test_preloaded_state():

    turn_history = [
        ("X", "A1"),
        ("O", "A2"),
        ("X", "B1"),
        ("O", "B2"),
        ("X", "C1"),
    ]

    #game = Game.from_turn_history(turn_history)
    game = Game(turn_history=turn_history)

    assert game.turn_history == turn_history
    assert game.board.get_square("A1").player_name == "X"
    assert game.board.get_square("A2").player_name == "O"
    assert game.board.get_square("B1").player_name == "X"
    assert game.board.get_square("B2").player_name == "O"
    assert game.board.get_square("C1").player_name == "X"
    assert game.board.winning_player_name == "X"
    #assert game.active_player_name == "X"


def test_play_from_preloaded_state():

    turn_history = [
        ("X", "A1"),
        ("O", "A2"),
        ("X", "B1"),
        #("O", "B2"),
        #("X", "C1"),
    ]
    #game = Game.from_turn_history(turn_history)
    game = Game(turn_history=turn_history)
    assert game.turn_history == turn_history
    assert game.board.get_square("A1").player_name == "X"
    assert game.board.get_square("A2").player_name == "O"
    assert game.board.get_square("B1").player_name == "X"
    assert game.board.get_square("B2").player_name == None
    assert game.board.get_square("C1").player_name == None
    assert game.board.winning_player_name == None
    assert game.active_player == "O"


    turn_history = [
        ("X", "A1"),
        ("O", "A2"),
        ("X", "B1"),
        ("O", "B2"),
        #("X", "C1"),
    ]
    game = Game(turn_history=turn_history)
    assert game.turn_history == turn_history
    assert game.board.get_square("A1").player_name == "X"
    assert game.board.get_square("A2").player_name == "O"
    assert game.board.get_square("B1").player_name == "X"
    assert game.board.get_square("B2").player_name == "O"
    assert game.board.get_square("C1").player_name == None
    assert game.board.winning_player_name == None
    assert game.active_player == "X"


    turn_history = [
        ("X", "A1"),
        ("O", "C2"),
        ("X", "B1"),
        ("O", "B2"),
        ("X", "C1"),
    ]
    game = Game(turn_history=turn_history)
    assert game.turn_history == turn_history
    assert game.board.get_square("A1").player_name == "X"
    assert game.board.get_square("C2").player_name == "O"
    assert game.board.get_square("B1").player_name == "X"
    assert game.board.get_square("B2").player_name == "O"
    assert game.board.get_square("C1").player_name == "X"
    assert game.board.winning_player_name == "X"
    assert game.active_player == "O"
