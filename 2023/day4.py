import re
from collections import defaultdict

filePath = "inputs/day4.txt"
def remvWhiteSpace(arr):
    return [i for i in arr if len(i)]

def splitNumbers(game):
    semiIndex, diviIndex = game.index(":"), game.index("|")
    winningNumbers, myNumbers = game[semiIndex + 2: diviIndex - 1].split(" "), game[diviIndex + 2:].rstrip("\n").split(" ")
    return remvWhiteSpace(winningNumbers),remvWhiteSpace(myNumbers)

def getGameId(game):
    gameData = game[:game.index(":")]
    gameId = re.split(r'\s+',gameData)[1]
    return int(gameId)
def luckyNumbers(inputFile):
    tsc = 0
    for game in inputFile:
        # print(game)
        cs = 0
        winningNumbers,myNumbers = splitNumbers(game)
        for number in myNumbers:
            if number.isdigit() and number in winningNumbers:
                cs = 1 if cs == 0 else cs * 2
        tsc += cs
    return tsc

def scratchCardsWon(inputFile):
    tCards,gameCopies = 0, defaultdict(lambda: 1)
    for game in inputFile:
        winningNumbers,myNumbers = splitNumbers(game)
        gameId = getGameId(game)
        tCards += gameCopies[gameId]
        matchingNums = len(set(winningNumbers).intersection(set(myNumbers)))
        for copys in range(1,matchingNums + 1):
            gameCopies[gameId + copys] += gameCopies[gameId]
    return tCards

with open(filePath, "r") as file:
    print(scratchCardsWon(file))
    file.close()
