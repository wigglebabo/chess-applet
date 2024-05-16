from pieces import Pawn, Rook, Bishop, Queen, Knight, King

class Board:
    def __init__(self, board: list)-> None:
        self.board = board

    def print_board(self):
        printboard = []
        for row in self.board :
            printrow = []
            for element in row :
                if not (element == "em") and (not element.taken):
                    if isinstance(element, Pawn):
                        if element.colour == "white":
                            printrow.append("wp")
                        else:
                            printrow.append("bp")
                    if isinstance(element, Rook):
                        if element.colour == "white":
                            printrow.append("wr")
                        else:
                            printrow.append("br")
                    if isinstance(element, King):
                        if element.colour == "white":
                            printrow.append("wk")
                        else:
                            printrow.append("bk")
                    if isinstance(element, Queen):
                        if element.colour == "white":
                            printrow.append("wq")
                        else:
                            printrow.append("bq")
                    if isinstance(element, Bishop):
                        if element.colour == "white":
                            printrow.append("wb")
                        else:
                            printrow.append("bb")
                    if isinstance(element, Knight):
                        if element.colour == "white":
                            printrow.append("wk")
                        else:
                            printrow.append("bk")
                else:
                    printrow.append("em")
            printboard.append(printrow)

        for r in printboard:
            print(r)

    def get_piece(self, posx: int, posy: int)->None:
        piece = self.board[posy][posx]
        return piece

    def replace_piece(self, xpos: int, ypos: int, piece: object or str)-> None:
        self.board[ypos][xpos] = piece


    def movepiece(self, xstart: int, ystart: int, xdest: int, ydest: int)-> None:
        if not self.get_piece(xstart, ystart) == "em":
            piece = self.get_piece(xstart, ystart)
            self.replace_piece(xdest, ydest, piece)
            self.replace_piece(xstart, ystart, "em")
        else:
            pass

