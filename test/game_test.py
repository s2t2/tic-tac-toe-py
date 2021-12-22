
from app.game import Game

# OUTCOMES
IN_PROGRESS = {'message': 'IN PROGRESS', 'reason': "IN_PROGRESS", 'winner': None}
X_WINS = {'message': 'X WINS!', 'reason': 'THREE_IN_A_ROW', 'winner': 'X'}
TIE = {'message': 'TIE', 'reason': 'NO_MORE_SQUARES', 'winner': None}

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

    # TEST WINNER OUTCOME

    game = Game()

    expected_outcomes = [
        {"turn": ("X", "A1"), "outcome": IN_PROGRESS},
        {"turn": ("O", "A2"), "outcome": IN_PROGRESS},
        {"turn": ("X", "B1"), "outcome": IN_PROGRESS},
        {"turn": ("O", "B2"), "outcome": IN_PROGRESS},
        {"turn": ("X", "C1"), "outcome": X_WINS},
    ]

    for d in expected_outcomes:
        player_name, square_name = d["turn"]
        game.board.set_square(square_name, player_name)
        assert game.outcome() == d["outcome"]

    # TEST TIE GAME OUTCOME

    game = Game()

    expected_outcomes = [
        {"turn": ("X", "A1"), "outcome": IN_PROGRESS},
        {"turn": ("O", "B2"), "outcome": IN_PROGRESS},
        {"turn": ("X", "B1"), "outcome": IN_PROGRESS},
        {"turn": ("O", "C1"), "outcome": IN_PROGRESS},
        {"turn": ("X", "A3"), "outcome": IN_PROGRESS},
        {"turn": ("O", "A2"), "outcome": IN_PROGRESS},
        {"turn": ("X", "C2"), "outcome": IN_PROGRESS},
        {"turn": ("X", "B3"), "outcome": IN_PROGRESS},
        {"turn": ("O", "C3"), "outcome": TIE},
    ]

    for d in expected_outcomes:
        player_name, square_name = d["turn"]
        game.board.set_square(square_name, player_name)
        print(game.board)
        assert game.outcome() == d["outcome"]



def test_compile_turn_history():

    turns = [
        ("X", "A1"),
        ("O", "A2"),
        ("X", "B1"),
        ("O", "B2"),
        ("X", "C1"),
    ]

    #game = Game()
    #game.take_turns(turns)
    #assert game.turn_history == turns

    game = Game()
    for turn in turns:
        game.take_turn(turn)
    assert game.turn_history == turns
    assert game.active_player == "O"
    assert game.outcome() == X_WINS
