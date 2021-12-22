

from app.square import Square

def test_squares():
    square = Square("A1")
    assert square.name == "A1"
    assert square.player_name == None
    assert square.player_label == " "

    square.player_name = "X"
    assert square.player_name == "X"
    assert square.player_label == "X"
