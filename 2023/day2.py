from functools import reduce
from operator import mul
file_path = "inputs/day2.txt"

def cubeGame(inputFile):
    colorMap = {"blue": 14, "green": 13, "red": 12}
    ans = 0
    for game in inputFile:
        semiIndex = game.index(":")
        gameInfo, gameData = game[5:semiIndex], game[semiIndex+2:].rstrip("\n").split("; ")
        gameFailed = False
        print(gameInfo, gameData)
        for show in gameData:
            showList = show.split(", ")
            showFailed = False
            for colorData in showList:
                value, color = colorData.split(" ")
                #print(value, color)
                if int(value) > colorMap[color]:
                    showFailed = True
                    break
            if showFailed:
                gameFailed = True
                break
        if not gameFailed:
            ans += int(gameInfo)
    return ans

def minCubes(inputFile):
    powerSetSum = 0
    for game in inputFile:
        semiIndex = game.index(":")
        gameInfo, gameData = game[5:semiIndex], game[semiIndex+2:].rstrip("\n").split("; ")
        #print(gameInfo, gameData)
        colorMap = {"red": 1, "blue": 1, "green": 1}
        for show in gameData:
            showList = show.split(", ")
            for colorData in showList:
                value, color = colorData.split(" ")
                colorMap[color] = max(colorMap[color],int(value))
        powerSet = reduce(mul,colorMap.values())
        #print(powerSet)
        powerSetSum += powerSet
    return powerSetSum

with open(file_path, "r") as file:
    #print(cubeGame(file))
    print(minCubes(file))
