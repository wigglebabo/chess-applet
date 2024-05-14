from piece import *




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