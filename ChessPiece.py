

from abc import ABC, abstractmethod

import Position, ChessBoard


class ChessPiece(ABC):

    @abstractmethod
    def is_legal_move(self, position:Position, board:ChessBoard):
        pass



class Pawn(ChessPiece):
    def is_legal_move(self, position: Position, board: ChessBoard):





        return