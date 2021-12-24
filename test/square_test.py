

from app.square import Square

def test_squares():
    square = Square("A1")
    assert square.name == "A1"
    assert square.letter == None
    assert square.label == " "
    assert square.is_selectable == True

    square.letter = "X"
    assert square.name == "A1"
    assert square.letter == "X"
    assert square.label == "X"
    assert square.is_selectable == False
