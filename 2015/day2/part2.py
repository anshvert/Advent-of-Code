filePath = "./input2.txt"

def volume(l,w,h):
    return l*w*h

def ribbon(l,w,h):
    sortedDimensions = sorted([l, w, h])
    return 2*(sortedDimensions[0] + sortedDimensions[1])

def ribbonRequired(file):
    totalRibbon = 0
    for dimensions in file:
        l,w,h = map(int, dimensions.split("x"))
        totalRibbon += volume(l,w,h) + ribbon(l,w,h)
    return totalRibbon

with open(filePath,"r") as file:
    print(ribbonRequired(file))