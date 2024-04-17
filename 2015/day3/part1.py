inputPath = "./input3.txt"

def calculateUniqueHouses(file):
    houses,iniCords = set(),[0,0]
    for directions in file:
        for direction in directions:
            if direction == "^":
                iniCords[1] += 1
            elif direction == "<":
                iniCords[0] += 1
            elif direction == ">":
                iniCords[0] -= 1
            else:
                iniCords[1] -= 1
            houses.add(tuple(iniCords))
    return len(houses)

with open(inputPath,"r") as file:
    print(calculateUniqueHouses(file))