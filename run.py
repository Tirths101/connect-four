import random # import random numbers

print("Welcome to Connect-IV")
print("_____________________")

potentialNumbers = ["I","II","III","IV","V","VI","VII"]
gameBoard = [["","","","","","",""], ["","","","","","",""], ["","","","","","",""],
["","","","","","",""], ["","","","","","",""], ["","","","","","",""]]

rows = 6
cols = 7

def printGameBoard():
    print("\n      I   II   III  IV    V   VI  VII  ", end="")
    for x in range(rows):
        print("\n   ------------------------------------")
        print(x, " |", end="")
        for y in range(cols):
            if(gameBoard[x][y] == "🏎️"):
                print("", gameBoard[x][y], end=" |")
            elif(gameBoard[x][y] == "🏍️"):
                print("", gameBoard[x][y], end=" |")
            else:
                print(" ", gameBoard[x][y], end="  |")
    print("\n   ------------------------------------")

printGameBoard()