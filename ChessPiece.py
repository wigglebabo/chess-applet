

from abc import ABC, abstractmethod

import Position, ChessBoard


class ChessPiece(ABC):

    @abstractmethod
    def is_legal_move(self, position:Position, board:ChessBoard):
        pass



class Pawn(ChessPiece):
    def is_legal_move(self, position: Position, board: ChessBoard, destination: Position):
        if (board.get_piece(destination) != None):
            legal_move = False
        




        return legal_move