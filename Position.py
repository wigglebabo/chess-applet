class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def position_from_notation(zet):

    #posY bepalen
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

    #posX bepalen
    if zet[1] == "1" :
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

    return Position(posX,posY)
