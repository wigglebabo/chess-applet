

from abc import ABC, abstractmethod

import Position, ChessBoard


class ChessPiece(ABC):

    @abstractmethod
    def is_legal_move(self, position:Position, board:ChessBoard, destination: Position):
        pass



class Pawn(ChessPiece):
    def is_legal_move(self, position: Position, board: ChessBoard, destination: Position):
        #er staat daar niets
        if (board.get_piece(destination) != None):
            legal_move = False
        #nie achteruit
        elif position.y < destination.y:
            legal_move = False
        #nie naar links/rechts
        elif (position.x != destination.x) and (board.get_piece(destination) == None):
            legal_move = False
        #nie meer dan 1 naar voor
        elif (position.y != 6) and ((position.x - destination.x) > 1):
            legal_move = False
        else:
            legal_move = True

        return legal_move