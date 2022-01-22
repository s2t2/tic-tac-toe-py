

class Square:
    def __init__(self, name):
        self.name = name
        self.letter = None

    def __repr__(self):
        return f"<Square {self.name}>"

    @property
    def label(self):
        return self.letter or " "

    @property
    def is_selectable(self):
        return not bool(self.letter)

    @property
    def is_selected(self):
        return bool(self.letter)

    @property
    def notation(self):
        return self.letter or "-"
