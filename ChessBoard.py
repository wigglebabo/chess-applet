from ChessPiece import ChessPiece
from Position import Position


class ChessBoard:


    def __init__(self):
        self.pieces = [
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None]
        ]



    def set_piece(self, piece:ChessPiece, position:Position):
        self.pieces[position.x][position.y] = piece

    def get_piece(self, position:Position):
        return self.pieces[position.x][position.y]

    def move_piece(self, start:Position, des:Position):
        piece = self.get_piece(start)

        self.set_piece(None, start)
        self.set_piece(piece, des)

