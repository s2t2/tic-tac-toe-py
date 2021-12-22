

class Square:
    def __init__(self, name):
        self.name = name
        self.player_name = None

    def __repr__(self):
        return f"<Square {self.name}>"

    @property
    def player_label(self):
        return self.player_name or " "
