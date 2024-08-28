"""
--- Part Two ---
In all the commotion, you realize that you forgot to seat yourself. At this point, you're pretty apathetic toward the whole thing,
and your happiness wouldn't really go up or down regardless of who you sit next to. You assume everyone else would be just as ambivalent about sitting next to you, too.

So, add yourself to the list, and give all happiness relationships that involve you a score of 0.

What is the total change in happiness for the optimal seating arrangement that actually includes yourself?
"""

from itertools import permutations

def KnightsOfDinner(inputFile):

    def getMutualHappyness(data):
        happiness = {}
        for line in data:
            words = line.split()
            person1 = words[0]
            person2 = words[-1][:-1]  # Remove the period at the end
            change = int(words[3]) if words[2] == "gain" else -int(words[3])

            if person1 not in happiness:
                happiness[person1] = {}
            happiness[person1][person2] = change

        return happiness

    def getTotalHappyness(setting):
        happyness,badEnergy = 0,float('inf')
        for i in range(len(setting)):
            p1,p2 = setting[i],setting[(i+1) % len(setting)]
            peerE = vibeDik[p1][p2] + vibeDik[p2][p1]
            happyness += peerE
            badEnergy = min(badEnergy,peerE)
        return happyness,badEnergy

    vibeDik = getMutualHappyness(inputFile)
    guests = list(vibeDik.keys())
    maxHappyness,badE = float('-inf'),float('inf')
    for arrangement in permutations(guests):
        totalHappyness,wE = getTotalHappyness(arrangement)
        if totalHappyness > maxHappyness:
            maxHappyness = totalHappyness
            badE = wE

    return maxHappyness - badE

filePath = "./input13.txt"

with open(filePath, "r") as file:
    print(KnightsOfDinner(file))