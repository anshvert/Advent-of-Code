filePath = "inputs/input2.txt"


def totalScore(inputFile):
    scoreGuide = {"A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3}
    score = 0
    for game in inputFile:
        plays = game.split(' ')
        oplay,mplay = plays[0],plays[1].rstrip("\n")
        #print(oplay,mplay)
        score += scoreGuide[mplay]
        if oplay == "A":
            if mplay == "X":
                score += 3
            elif mplay == "Y":
                score += 6
        elif oplay == "B":
            if mplay == "Y":
                score += 3
            elif mplay == "Z":
                score += 6
        else:
            if mplay == "Z":
                score += 3
            elif mplay == "X":
                score += 6
        #print(score)
    return score

def secretScore(inputFile):
    score = 0
    for game in inputFile:
        plays = game.split(' ')
        oplay,mplay = plays[0],plays[1].rstrip("\n")
        #print(oplay,mplay)
        if oplay == "A":
            if mplay == "X":
                score += 3
            elif mplay == "Y":
                score += 4
            else:
                score += 8
        elif oplay == "B":
            if mplay == "X":
                score += 1
            elif mplay == "Y":
                score += 5
            else:
                score += 9
        else:
            if mplay == "X":
                score += 2
            elif mplay == "Y":
                score += 6
            else:
                score += 7
    return score
with open(filePath, "r") as file:
    print(secretScore(file))
