
#from tkinter import *



#def click():
    #print("hello")

#window = Tk()
#button = Button(window, text="click me!!!")
#button.config(command=click)
#button.config(font=("Ink Free", 50, "bold"))
#button.config(bg='#ff6200')
#button.config(fg='#fffb1f')
#button.pack()
#window.mainloop()

import time

turn = 0
mat = False
board = [
         ["bT","bP","bL","bD","bK","bL","bP","bT"],
         ["bp","bp","bp","bp","bp","bp","bp","bp"],
         ["em","em","em","em","em","em","em","em"],
         ["em","em","em","em","em","em","em","em"],
         ["em","em","em","em","em","em","em","em"],
         ["em","em","em","em","em","em","em","em"],
         ["wp","wp","wp","wp",":D","wp","wp","wp"],
         ["wT","wP","wL","wD","wK","wL","wP","wT"]
         ]
def printboard():
    for i in board:
        for j in i:
            print(j, end=" ")
        print()
#bepaal de positie op de array met schaakcoordinaten
def waarOpHetBoard(zet):
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
    #return value
    return(posY,posX)


printboard()
print("de notatie gaat als volgt: eerst het stuk: p (kleine) voor pion, T voor toren, P(grote) voor paard, L voor loper, D voor dame, K voor koning.")
print("de coordinaten gaan zoals een normaal schaakspel.")
print("veel succes!")


while not mat:
    if (turn % 2) == 0:
        print("Wit aan zet")
    else:
        print("Zwart aan zet")
    stuk = input("welk stuk wil je zetten? ")
    posStuk = input("waar staat het stuk? ")
    desStuk = input("naar waar gaat het stuk? " )
    #confirmation voor je zet
    confirm = input("is dit je zet: " + stuk + " op " + posStuk + " naar " + desStuk + " ? y/n ")
    if confirm == "y":
        print(board[int(str(waarOpHetBoard(posStuk))[1])] [int(str(waarOpHetBoard(posStuk))[4])])
        turn = turn + 1