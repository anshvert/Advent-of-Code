filePath = "inputs/day3.txt"


def validPos(x, y, mat):
    return 0 <= x < len(mat) and 0 <= y < len(mat[0])


def getNumIndex(x, y, mat, dirc):
    cI = y
    if dirc == -1:
        while y >= 0 and mat[x][y].isdigit():
            cI = y
            y -= 1
    else:
        while y < len(mat[0]) and mat[x][y].isdigit():
            cI = y
            y += 1
    return cI


def checkNums(x, y, mat, indexSet):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, -1), (1, -1), (1, 1), (-1, 1)]
    symVal,symCount,symSet = 1,0,set()
    for xx, yy in dirs:
        newX, newY = x + xx, y + yy
        if validPos(newX, newY, mat):
            if mat[newX][newY].isdigit():
                lIndex = getNumIndex(newX, newY, mat, -1)
                rIndex = getNumIndex(newX, newY, mat, 1)
                if (newX,lIndex,rIndex) in symSet:
                    continue
                symSet.add((newX,lIndex,rIndex))
                # if (newX, lIndex, rIndex) in indexSet:
                #     continue
                # indexSet.add((newX, lIndex, rIndex))
                # print(lIndex,rIndex)
                # print(mat[newX][lIndex:rIndex+1])
                curVal = int("".join(mat[newX][lIndex:rIndex + 1]))
                # print(curVal)
                symVal *= curVal
                symCount += 1

    #print(symVal,symCount)
    return symVal if symCount == 2 else 0


def engineNumbers(inputFile):
    symbols = ["*", "#", "+", "$", "!", "@", "%", "^", "&", "=", "/", "-"]
    mat, numIndexSet, tsm = [], set(), 0
    for engLine in inputFile:
        # print(engLine)
        mat.append(list(engLine.rstrip("\n")))
    # print(mat)
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] in symbols:
                tsm += checkNums(i, j, mat, numIndexSet)
    return tsm


with open(filePath, "r") as file:
    print(engineNumbers(file))
    file.close()
