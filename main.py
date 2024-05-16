from pieces import Piece, Pawn, Rook, Bishop, Queen, Knight, King
from board import Board


mat = False

def reset_board():
    mat = False
    # define all the pieces
    # the pawns
    bp1 = Pawn(0, 1, "black", False)
    bp2 = Pawn(1, 1, "black", False)
    bp3 = Pawn(2, 1, "black", False)
    bp4 = Pawn(3, 1, "black", False)
    bp5 = Pawn(4, 1, "black", False)
    bp6 = Pawn(5, 1, "black", False)
    bp7 = Pawn(6, 1, "black", False)
    bp8 = Pawn(7, 1, "black", False)

    wp1 = Pawn(0, 6, "white", False)
    wp2 = Pawn(1, 6, "white", False)
    wp3 = Pawn(2, 6, "white", False)
    wp4 = Pawn(3, 6, "white", False)
    wp5 = Pawn(4, 6, "white", False)
    wp6 = Pawn(5, 6, "white", False)
    wp7 = Pawn(6, 6, "white", False)
    wp8 = Pawn(7, 6, "white", False)

    # the rooks
    br1 = Rook(0, 0, "black", False)
    br2 = Rook(7, 0, "black", False)
    wr1 = Rook(0, 7, "white", False)
    wr2 = Rook(7, 7, "white", False)

    # the bishops
    bb1 = Bishop(2, 0, "black", False)
    bb2 = Bishop(5, 0, "black", False)
    wb1 = Bishop(2, 7, "white", False)
    wb2 = Bishop(5, 7, "white", False)

    # the knights
    bk1 = Knight(1, 0, "black", False)
    bk2 = Knight(6, 0, "black", False)
    wk1 = Knight(1, 7, "white", False)
    wk2 = Knight(6, 7, "white", False)

    # the Queens
    bq = Queen(3, 0, "black", False)
    wq = Queen(3, 7, "white", False)

    # the kings
    bk = King(4, 0, "black", False)
    wk = King(4, 7, "white", False)

    bOard = [
        [br1, bk1, bb1, bq, bk, bb2, bk2, br2],
        [bp1, bp2, bp3, bp4, bp5, bp6, bp7, bp8],
        ["em", "em", "em", "em", "em", "em", "em", "em"],
        ["em", "em", "em", "em", "em", "em", "em", "em"],
        ["em", "em", "em", "em", "em", "em", "em", "em"],
        ["em", "em", "em", "em", "em", "em", "em", "em"],
        [wp1, wp2, wp3, wp4, wp5, wp6, wp7, wp8],
        [wr1, wk1, wb1, wq, wk, wb2, wk2, wr2],
    ]

    board = Board(bOard)

    return board

# notation to coordinates
def position_from_notation(zet):
    posX = 0
    posY = 0
    # posX bepalen
    if zet[0].lower() == "a":
        posX = 0
    elif zet[0].lower() == "b":
        posX = 1
    elif zet[0].lower() == "c":
        posX = 2
    elif zet[0].lower() == "d":
        posX = 3
    elif zet[0].lower() == "e":
        posX = 4
    elif zet[0].lower() == "f":
        posX = 5
    elif zet[0].lower() == "g":
        posX = 6
    elif zet[0].lower() == "h":
        posX = 7
    # posY bepalen
    if zet[1] == "1":
        posY = 7
    elif zet[1] == "2":
        posY = 6
    elif zet[1] == "3":
        posY = 5
    elif zet[1] == "4":
        posY = 4
    elif zet[1] == "5":
        posY = 3
    elif zet[1] == "6":
        posY = 2
    elif zet[1] == "7":
        posY = 1
    elif zet[1] == "8":
        posY = 0
    # return value
    return (posY, posX)


bp1 = Pawn(0, 1, "black", False)
bp2 = Pawn(1, 1, "black", False)
bp3 = Pawn(2, 1, "black", False)
bp4 = Pawn(3, 1, "black", False)
bp5 = Pawn(4, 1, "black", False)
bp6 = Pawn(5, 1, "black", False)
bp7 = Pawn(6, 1, "black", False)
bp8 = Pawn(7, 1, "black", False)

wp1 = Pawn(0, 6, "white", False)
wp2 = Pawn(1, 6, "white", False)
wp3 = Pawn(2, 6, "white", False)
wp4 = Pawn(3, 6, "white", False)
wp5 = Pawn(4, 6, "white", False)
wp6 = Pawn(5, 6, "white", False)
wp7 = Pawn(6, 6, "white", False)
wp8 = Pawn(7, 6, "white", False)

    # the rooks
br1 = Rook(0, 0, "black", False)
br2 = Rook(7, 0, "black", False)
wr1 = Rook(0, 7, "white", False)
wr2 = Rook(7, 7, "white", False)

    # the bishops
bb1 = Bishop(2, 0, "black", False)
bb2 = Bishop(5, 0, "black", False)
wb1 = Bishop(2, 7, "white", False)
wb2 = Bishop(5, 7, "white", False)

    # the knights
bk1 = Knight(1, 0, "black", False)
bk2 = Knight(6, 0, "black", False)
wk1 = Knight(1, 7, "white", False)
wk2 = Knight(6, 7, "white", False)

    # the Queens
bq = Queen(3, 0, "black", False)
wq = Queen(3, 7, "white", False)

    # the kings
bk = King(4, 0, "black", False)
wk = King(4, 7, "white", False)

# game loop start
mat = False

board = reset_board()

board.print_board()


print("de coordinaten gaan zoals een normaal schaakspel.")
print("veel succes!")

while not mat:
    start = input("van waar? ")
    dest = input("naar waar? ")
    start_cords = position_from_notation(start)
    dest_cords = position_from_notation(dest)
    board.movepiece(start_cords[1], start_cords[0], dest_cords[1], dest_cords[0])

    board.print_board()

    mss_mat = input("is het mat? y/n ")
    if mss_mat.lower() == "y":
        mat = True





