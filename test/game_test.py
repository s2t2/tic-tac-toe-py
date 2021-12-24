
from app.game import Game
from conftest import (
    X_WINS_TURNS, TIE_GAME_TURNS, IN_PROGRESS_TURNS,
    X_WINS_OUTCOME, TIE_GAME_OUTCOME
)

def test_toggle_active_player():
    game = Game()
    #assert game.active_player == None

    #game.toggle_active_player()
    assert game.active_player.letter == "X"

    game.toggle_active_player()
    assert game.active_player.letter == "O"

    game.toggle_active_player()
    assert game.active_player.letter == "X"

    game.toggle_active_player()
    assert game.active_player.letter == "O"


def test_preloaded_state():

    # IN PROGRESS GAME ("O" PLAYER IS NEXT)

    turn_history = [
        ("X", "A1"),
        ("O", "A2"),
        ("X", "B1"),
    ]
    game = Game(turn_history=turn_history)
    assert game.turn_history == turn_history
    assert game.board.get_square("A1").letter == "X"
    assert game.board.get_square("A2").letter == "O"
    assert game.board.get_square("B1").letter == "X"
    assert game.board.get_square("B2").letter == None
    assert game.board.get_square("C1").letter == None
    assert game.board.winner == None
    assert game.board.outcome == None
    assert game.active_player.letter == "O"

    # IN PROGRESS GAME ("X" PLAYER IS NEXT)

    turn_history = [
        ("X", "A1"),
        ("O", "A2"),
        ("X", "B1"),
        ("O", "B2"),
    ]
    game = Game(turn_history=turn_history)
    assert game.turn_history == turn_history
    assert game.board.get_square("A1").letter == "X"
    assert game.board.get_square("A2").letter == "O"
    assert game.board.get_square("B1").letter == "X"
    assert game.board.get_square("B2").letter == "O"
    assert game.board.get_square("C1").letter == None
    assert game.board.winner == None
    assert game.board.outcome == None
    assert game.active_player.letter == "X"

    # COMPLETED GAME (HAS WINNER AND OUTCOME)

    turn_history = [
        ("X", "A1"),
        ("O", "A2"),
        ("X", "B1"),
        ("O", "B2"),
        ("X", "C1"),
    ]
    game = Game(turn_history=turn_history)
    assert game.turn_history == turn_history
    assert game.board.get_square("A1").letter == "X"
    assert game.board.get_square("A2").letter == "O"
    assert game.board.get_square("B1").letter == "X"
    assert game.board.get_square("B2").letter == "O"
    assert game.board.get_square("C1").letter == "X"
    assert game.winner == X_WINS_OUTCOME["winner"]
    assert game.outcome == X_WINS_OUTCOME
    assert game.active_player.letter == "O" # this will be the case, although it isn't an important / desired part of the design. could as well be null and the player cycling turned off or something.


def test_take_turns():

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
    assert game.active_player.letter == "O"
    assert game.outcome == X_WINS_OUTCOME

    # TAKE TURNS

    game = Game()
    game.take_turns(turns)
    assert game.turn_history == turns
    assert game.active_player.letter == "O"
    assert game.outcome == X_WINS_OUTCOME



def test_outcome():

    # won games
    game = Game(turn_history=X_WINS_TURNS)
    outcome = game.outcome
    assert isinstance(outcome, dict) # assert isinstance(outcome, Outcome)
    assert outcome == X_WINS_OUTCOME
    #assert outcome.winner == {'player_name': 'X', 'square_names': ['A1', 'B1', 'C1']}
    #assert outcome.reason == "THREE_IN_A_ROW"
    #assert outcome.message == "X WINS!"
    #assert outcome.winning_player_name == "X"
    #assert outcome.winning_square_names == ['A1', 'B1', 'C1']

    # tie games
    game = Game(turn_history=TIE_GAME_TURNS)
    outcome = game.outcome
    assert isinstance(outcome, dict) # assert isinstance(outcome, Outcome)
    assert outcome == TIE_GAME_OUTCOME
    #assert outcome.winner == None
    #assert outcome.reason == "NO_MORE_SQUARES"
    #assert outcome.message == "TIE GAME"
    #assert outcome.winning_player_name == None
    #assert outcome.winning_square_names == None

    # in-progress games have no outcome
    game = Game(turn_history=IN_PROGRESS_TURNS)
    outcome = game.outcome
    assert outcome == None

    # not yet started games have no outcome
    game = Game()
    outcome = game.outcome
    assert outcome == None
