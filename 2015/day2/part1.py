filePath = "./input2.txt"

def surfaceArea(l,w,h):
    return 2*(l*w + w*h + h*l)

def extraPaper(l,w,h):
    sortedDimensions = sorted([l,w,h])
    return sortedDimensions[0]*sortedDimensions[1]

def totalWrappingPaper(file):
    totalPaper = 0
    for dimensions in file:
        l,w,h = map(int,dimensions.split("x"))
        totalPaper += surfaceArea(l,w,h) + extraPaper(l,w,h)
    return totalPaper

with open(filePath,"r") as file:
    print(totalWrappingPaper(file))