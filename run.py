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

def modifyArray(positionPicked, turn):
    gameBoard[positionPicked[0]][positionPicked[1]] = turn

def checkForWinner(chip):
    # Check the horizontal spaces
    for y in range(rows):
        for x in range(cols - 3):
            if (gameBoard[x][y] == chip and gameBoard[x+1][y] == chip and gameBoard[x+2][y] == chip and gameBoard[x+3][y] == chip):
                print("\nGame over!", chip, " wins! Thank you playing")
                return True

    # Check the vertical spaces
    for y in range(rows):
        for x in range(cols - 3):
            if (gameBoard[x][y] == chip and gameBoard[x][y+1] == chip and gameBoard[x][y+2] == chip and gameBoard[x][y+3] == chip):
                print("\nGame over!", chip, " wins! Thank you playing")
                return True

    # Check the diagonal (from top right to bottom left) spaces
    for y in range(rows - 3):
        for x in range(3, cols):
            if (gameBoard[x][y] == chip and gameBoard[x+1][y-1] == chip and gameBoard[x+2][y-2] == chip and gameBoard[x+3][y-3] == chip):
                print("\nGame over!", chip, " wins! Thank you playing")
                return True

    # Check the diagonal (from top left to bottom right) spaces
    for y in range(rows - 3):
        for x in range(cols - 3):
            if (gameBoard[x][y] == chip and gameBoard[x+1][y+1] == chip and gameBoard[x+2][y+2] == chip and gameBoard[x+3][y+3] == chip):
                print("\nGame over!", chip, " wins! Thank you playing")
                return True

    return False

def coordinateParser(inputString):
    coordinate = [None] * 2
    if(inputString[0] == "I"):
        coordinate[1] = 0
    elif(inputString[0] == "II"):
        coordinate[1] = 1
    elif(inputString[0] == "III"):
        coordinate[1] = 2
    elif(inputString[0] == "IV"):
        coordinate[1] = 3
    elif(inputString[0] == "V"):
        coordinate[1] = 4
    elif(inputString[0] == "VI"):
        coordinate[1] = 5
    elif(inputString[0] == "VII"):
        coordinate[1] = 6
    else:
        print("Invalid")
    coordinate[0] = int(inputString[1])
    return coordinate

def isSpaceAvailable(intendedCoordinate):
    if(gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🏎️'):
        return False
    elif(gameBoard[intendedCoordinate[0]][intendedCoordinate[1]] == '🏍️'):
        return False
    else:
        True

def gravityChecker(intendedCoordinate):
    # Calculate space below
    spaceBelow = [None] * 2
    spaceBelow[0] = intendedCoordinate[0] + 1
    spaceBelow[1] = intendedCoordinate[1]
    # Is the coordinate at ground level 
    if(spaceBelow[0] == 6):
        return True
    # Check if there's a token below
    if(isSpaceAvailable(spaceBelow) == False):
        return True
    return False

    
turnCounter = 0
while True:
    if(turnCounter % 2 == 0):
        printGameBoard()
        while True:
            positionPicked = input("\nChoose a position: ")
            coordinate = coordinateParser(positionPicked)
            try:
                # Check if the space is available
                if(isSpaceAvailable(coordinate) and gravityChecker(coordinate)):
                    modifyArray(coordinate, '🏍️')
                    break
                else:
                    print("Not a valid coordinate")
            except:
                print("Error occured. Please try again.")
        winner = checkForWinner('🏍️')
        turnCounter += 1
    # It's the computers turn
    else:
        while True:
            cpuChoice = [random.choice(potentialNumbers), random.randint(0,5)]
            cpuCoordinate = coordinateParser(cpuChoice)
            if(isSpaceAvailable(cpuCoordinate) and gravityChecker(cpuCoordinate)):
                modifyArray(coordinate, '🏎️')
                break
        turnCounter += 1
        winner = checkForWinner('🏎️')

    if(winner):
        printGameBoard()
        break
             