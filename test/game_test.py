
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


def test_outcome_determination():

    in_progress = {'message': 'IN PROGRESS', 'reason': "IN_PROGRESS", 'winner': None}
    x_wins = {'message': 'X WINS!', 'reason': 'THREE_IN_A_ROW', 'winner': 'X'}
    tie = {'message': 'TIE', 'reason': 'NO_MORE_SQUARES', 'winner': None}

    # TEST WINNER OUTCOME

    game = Game()

    expected_outcomes = [
        {"turn": ("X", "A1"), "outcome": in_progress},
        {"turn": ("O", "A2"), "outcome": in_progress},
        {"turn": ("X", "B1"), "outcome": in_progress},
        {"turn": ("O", "B2"), "outcome": in_progress},
        {"turn": ("X", "C1"), "outcome": x_wins},
    ]

    for d in expected_outcomes:
        player_name, square_name = d["turn"]
        game.board.set_square(square_name, player_name)
        assert game.outcome() == d["outcome"]

    # TEST TIE GAME OUTCOME

    game = Game()

    expected_outcomes = [
        {"turn": ("X", "A1"), "outcome": in_progress},
        {"turn": ("O", "B2"), "outcome": in_progress},
        {"turn": ("X", "B1"), "outcome": in_progress},
        {"turn": ("O", "C1"), "outcome": in_progress},
        {"turn": ("X", "A3"), "outcome": in_progress},
        {"turn": ("O", "A2"), "outcome": in_progress},
        {"turn": ("X", "C2"), "outcome": in_progress},
        {"turn": ("X", "B3"), "outcome": in_progress},
        {"turn": ("O", "C3"), "outcome": tie},
    ]

    for d in expected_outcomes:
        player_name, square_name = d["turn"]
        game.board.set_square(square_name, player_name)
        print(game.board)
        assert game.outcome() == d["outcome"]
