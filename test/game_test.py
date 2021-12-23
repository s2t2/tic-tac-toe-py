
from app.game import Game
#from app.outcome import Outcome

from conftest import X_WINS, TIE_GAME, IN_PROGRESS

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
    #assert game.board.winner == None
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
    #assert game.board.winner == None
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
    #assert game.board.winner["player_name"] == "X"
    assert game.active_player == "O"


def test_compile_turn_history():

    turns = [
        ("X", "A1"),
        ("O", "A2"),
        ("X", "B1"),
        ("O", "B2"),
        ("X", "C1"),
    ]

    # TAKE TURN

    game = Game()
    for turn in turns:
        game.take_turn(turn)
    assert game.turn_history == turns
    assert game.active_player == "O"
    assert game.outcome["winner"]["player_name"] == "X"

    # TAKE TURNS

    game = Game()
    game.take_turns(turns)
    assert game.turn_history == turns
    assert game.active_player == "O"
    assert game.outcome["winner"]["player_name"] == "X"


def test_outcome():

    # won games
    game = Game(turn_history=X_WINS)
    #outcome = game.outcome
    #assert isinstance(outcome, Outcome)
    #assert outcome.winner == {'player_name': 'X', 'square_names': ['A1', 'B1', 'C1']}
    #assert outcome.reason == "THREE_IN_A_ROW"
    #assert outcome.message == "X WINS!"
    #assert outcome.winning_player_name == "X"
    #assert outcome.winning_square_names == ['A1', 'B1', 'C1']
    assert game.outcome == {
        'message': 'X WINS!',
        'reason': 'THREE_IN_A_ROW',
        'winner': {
            'player_name': 'X',
            'square_names': ['A1', 'B1', 'C1']
        }
    }

    # tie games
    game = Game(turn_history=TIE_GAME)
    #outcome = game.outcome
    #assert isinstance(outcome, Outcome)
    #assert outcome.reason == "NO_MORE_SQUARES"
    #assert outcome.message == "TIE GAME"
    #assert outcome.winning_player_name == None
    #assert outcome.winning_square_names == None
    assert game.outcome == {
        'message': 'TIE GAME',
        'reason': 'NO_MORE_SQUARES',
        'winner': None
    }

    # in-progress games have no outcome
    game = Game(turn_history=IN_PROGRESS)
    outcome = game.outcome
    assert outcome == None

    # not yet started games have no outcome
    game = Game()
    outcome = game.outcome
    assert outcome == None
