
class Piece:
    def __init__(self, xpos: int, ypos: int, colour: str, taken: bool) -> None:
        self.xpos = xpos
        self.ypos = ypos
        self.colour = colour
        self.taken = taken


class Pawn(Piece):
    def __init__(self, xpos: int, ypos: int, colour: str, taken: bool) -> None:
        super().__init__(xpos=xpos, ypos=ypos, colour=colour, taken=taken)


class Rook(Piece):
    def __init__(self, xpos: int, ypos: int, colour: str, taken: bool) -> None:
        super().__init__(xpos=xpos, ypos=ypos, colour=colour, taken=taken)


class Bishop(Piece):
    def __init__(self, xpos: int, ypos: int, colour: str, taken: bool) -> None:
        super().__init__(xpos=xpos, ypos=ypos, colour=colour, taken=taken)

class Knight(Piece):
    def __init__(self, xpos: int, ypos: int, colour: str, taken: bool) -> None:
        super().__init__(xpos=xpos, ypos=ypos, colour=colour, taken=taken)

class Queen(Piece):
    def __init__(self, xpos: int, ypos: int, colour: str, taken: bool) -> None:
        super().__init__(xpos=xpos, ypos=ypos, colour=colour, taken=taken)

class King(Piece):

    def __init__(self, xpos: int, ypos: int, colour: str, taken: bool) -> None:
        super().__init__(xpos=xpos, ypos=ypos, colour=colour, taken=taken)


