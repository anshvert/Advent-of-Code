filePath = "input1.txt"

def checkBaseMent(file):
    floor,cPos = 0,0
    for paren in file:
        for chrc in paren:
            cPos += 1
            if chrc == "(":
                floor += 1
            else:
                floor -= 1
            if floor == -1:
                return cPos

with open(filePath,"r") as file:
    print(checkBaseMent(file))