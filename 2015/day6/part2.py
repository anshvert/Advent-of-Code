"""
--- Part Two ---
You just finish implementing your winning light pattern when you realize you mistranslated Santa's message from Ancient Nordic Elvish.

The light grid you bought actually has individual brightness controls; each light can have a brightness of zero or more. The lights all start at zero.

The phrase turn on actually means that you should increase the brightness of those lights by 1.

The phrase turn off actually means that you should decrease the brightness of those lights by 1, to a minimum of zero.

The phrase toggle actually means that you should increase the brightness of those lights by 2.

What is the total brightness of all lights combined after following Santa's instructions?

For example:

turn on 0,0 through 0,0 would increase the total brightness by 1.
toggle 0,0 through 999,999 would increase the total brightness by 2000000.
"""

from collections import defaultdict

inputPath = "./input6.txt"

def turnLight(lightMap,initialPos,endingPos,value):
    for i in range(initialPos[0],endingPos[0]+1):
        for j in range(initialPos[1],endingPos[1]+1):
            lightMap[(i,j)] += value
            lightMap[(i,j)] = max(lightMap[(i,j)],0)

def getValueFromString(string):
    x,y = string.strip().split(",")
    return int(x),int(y)

def theLights(file):
    lightMap = defaultdict(int)
    for instructions in file:
        leftInstruction,rightInstruction = instructions.split("through")
        leftInstructionCommands = leftInstruction.split()
        startingPos,endingPos = getValueFromString(leftInstructionCommands[-1]),getValueFromString(rightInstruction)
        if leftInstructionCommands[0] == "turn":
            if leftInstructionCommands[1] == "on":
                turnLight(lightMap,startingPos,endingPos,1)
            elif leftInstructionCommands[1] == "off":
                turnLight(lightMap,startingPos,endingPos,-1)
        else:
            turnLight(lightMap,startingPos,endingPos,2)
    return sum(lightMap.values())

with open(inputPath,"r") as file:
    print(theLights(file))