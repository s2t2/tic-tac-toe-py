


#from app.outcome import Outcome
#from app.game import TIE_REASON, WIN_REASON
#
#def test_outcome():
#
#    # won games
#    winner = {'player_name': 'X', 'square_names': ['A1', 'B1', 'C1']}
#    outcome = Outcome(reason=WIN_REASON, winner=winner)
#    assert isinstance(outcome, Outcome)
#    assert outcome.winner == {'player_name': 'X', 'square_names': ['A1', 'B1', 'C1']}
#    assert outcome.reason == "THREE_IN_A_ROW"
#    assert outcome.message == "X WINS!"
#    assert outcome.winning_player_name == "X"
#    assert outcome.winning_square_names == ['A1', 'B1', 'C1']
#
#    # tie games
#
#    outcome = Outcome(TIE_REASON, winner=None)
#    assert isinstance(outcome, Outcome)
#    assert outcome.winner == None
#    assert outcome.reason == "NO_MORE_SQUARES"
#    assert outcome.message == "TIE GAME"
#    assert outcome.winning_player_name == None
#    assert outcome.winning_square_names == None
#






#def test_outcome():
#
#    # won games
#    game = Game(turn_history=X_WINS)
#    outcome = game.outcome
#    #assert isinstance(outcome, Outcome)
#    assert outcome != None
#    assert outcome.winner == {'player_name': 'X', 'square_names': ['A1', 'B1', 'C1']}
#    assert outcome.reason == "THREE_IN_A_ROW"
#    assert outcome.message == "X WINS!"
#    assert outcome.winning_player_name == "X"
#    assert outcome.winning_square_names == ['A1', 'B1', 'C1']
#
#    # tie games
#    game = Game(turn_history=TIE_GAME)
#    outcome = game.outcome
#    assert isinstance(outcome, Outcome)
#    assert outcome.winner == None
#    assert outcome.reason == "NO_MORE_SQUARES"
#    assert outcome.message == "TIE GAME"
#    assert outcome.winning_player_name == None
#    assert outcome.winning_square_names == None
#
#    # in-progress games have no outcome
#    game = Game(turn_history=IN_PROGRESS)
#    outcome = game.outcome
#    assert outcome == None
#
#    # not yet started games have no outcome
#    game = Game()
#    outcome = game.outcome
#    assert outcome == None
