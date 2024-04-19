"""
--- Day 6: Probably a Fire Hazard ---
Because your neighbors keep defeating you in the holiday house decorating contest year after year, you've decided to deploy one million lights in a 1000x1000 grid.

Furthermore, because you've been especially nice this year, Santa has mailed you instructions on how to display the ideal lighting configuration.

Lights in your grid are numbered from 0 to 999 in each direction; the lights at each corner are at 0,0, 0,999, 999,999, and 999,0. The instructions include whether to turn on, turn off, or toggle various inclusive ranges given as coordinate pairs.
Each coordinate pair represents opposite corners of a rectangle, inclusive; a coordinate pair like 0,0 through 2,2 therefore refers to 9 lights in a 3x3 square. The lights all start turned off.

To defeat your neighbors this year, all you have to do is set up your lights by doing the instructions Santa sent you in order.

For example:

turn on 0,0 through 999,999 would turn on (or leave on) every light.
toggle 0,0 through 999,0 would toggle the first line of 1000 lights, turning off the ones that were on, and turning on the ones that were off.
turn off 499,499 through 500,500 would turn off (or leave off) the middle four lights.
After following the instructions, how many lights are lit?
"""
from collections import defaultdict

inputPath = "./input6.txt"

def turnLight(lightMap,initialPos,endingPos,value):
    for i in range(initialPos[0],endingPos[0]+1):
        for j in range(initialPos[1],endingPos[1]+1):
            lightMap[(i,j)] = value

def getValueFromString(string):
    x,y = string.strip().split(",")
    return int(x),int(y)

def toggle(lightMap,initialPos,endingPos):
    for i in range(initialPos[0],endingPos[0]+1):
        for j in range(initialPos[1],endingPos[1]+1):
            lightMap[(i,j)] ^= 1

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
                turnLight(lightMap,startingPos,endingPos,0)
        else:
            toggle(lightMap,startingPos,endingPos)
    return sum(lightMap.values())

with open(inputPath,"r") as file:
    print(theLights(file))
