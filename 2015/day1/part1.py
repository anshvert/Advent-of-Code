filePath = "input1.txt"

def checkFloor(file):
    up,down = 0,0
    for paren in file:
        for chrc in paren:
            if chrc == "(":
                up += 1
            else:
                down += 1
    return up - down

with open(filePath,"r") as file:
    print(checkFloor(file))