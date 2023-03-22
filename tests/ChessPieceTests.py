import unittest

from ChessBoard import ChessBoard
from ChessPiece import Pawn
from Position import Position, position_from_notation


class ChessPieceTest(unittest.TestCase):
    def test_white_pawn_forward(self):
        board = ChessBoard()
        pawn = Pawn()

        board.set_piece(pawn, position_from_notation("E4"))
        legal_move = pawn.is_legal_move(position_from_notation("E5"), board)

        self.assertEqual(True, legal_move)

    def test_white_pawn_backwards(self):
        board = ChessBoard()
        pawn = Pawn()

        board.set_piece(pawn, position_from_notation("E4"))
        legal_move = pawn.is_legal_move(position_from_notation("E3"), board)

        self.assertEqual(False, legal_move)





class ChessBoardTest(unittest.TestCase):
    def test_get_piece(self):
        board = ChessBoard()
        pawn = Pawn()

        board.set_piece(pawn, position_from_notation("e4"))
        piece = board.get_piece(position_from_notation("e4"))

        self.assertEqual(pawn, piece)

    def test_new_board_no_pieces(self):
        board = ChessBoard()

        piece = board.get_piece(position_from_notation("e4"))

        self.assertEqual(None, piece)

    def test_move_piece(self):
        board = ChessBoard()
        pawn = Pawn()

        board.set_piece(pawn, position_from_notation("e4"))
        board.move_piece(position_from_notation("e4"), position_from_notation("e5"))

        piece = board.get_piece(position_from_notation("e5"))

        self.assertEqual(pawn, piece)
        self.assertEqual(None, board.get_piece(position_from_notation("e4")))




if __name__ == '__main__':
    unittest.main()
