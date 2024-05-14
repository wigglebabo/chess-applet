from piece import *
from board import *




# define all the pieces
# the pawns
bp1 = Pawn(0,1,"black",False)
bp2 = Pawn(1,1,"black",False)
bp3 = Pawn(2,1,"black",False)
bp4 = Pawn(3,1,"black",False)
bp5 = Pawn(4,1,"black",False)
bp6 = Pawn(5,1,"black",False)
bp7 = Pawn(6,1,"black",False)
bp8 = Pawn(7,1,"black",False)

wp1 = Pawn(0,6,"white",False)
wp2 = Pawn(1,6,"white",False)
wp3 = Pawn(2,6,"white",False)
wp4 = Pawn(3,6,"white",False)
wp5 = Pawn(4,6,"white",False)
wp6 = Pawn(5,6,"white",False)
wp7 = Pawn(6,6,"white",False)
wp8 = Pawn(7,6,"white",False)

# the rooks
br1 = Rook(0,0,"black",False)
br2 = Rook(7,0,"black",False)
wr1 = Rook(0,7,"white",False)
wr2 = Rook(7,7,"white", False)

# the bishops
bb1 = Bishop(2,0,"black",False)
bb2 = Bishop(5,0,"black",False)
wb1 = Bishop(2,7,"white",False)
wb2 = Bishop(5,7,"white",False)

# the knights
bk1 = Knight(1,0,"black",False)
bk2 = Knight(6,0,"black",False)
wk1 = Knight(1,7,"white",False)
wk2 = Knight(6,7,"white",False)

# the Queens
bq = Queen(3,0,"black",False)
wq = Queen(3,7,"white",False)

# the kings
bk = King(4,0,"black",False)
wk = King(4,7,"white",False)

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

board.print_board()



