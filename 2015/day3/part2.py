inputPath = "./input3.txt"

def uniqueHouses(path):
    houses,iniCords = set(), [0, 0]
    for direction in path:
        if direction == "^":
            iniCords[1] += 1
        elif direction == "<":
            iniCords[0] += 1
        elif direction == ">":
            iniCords[0] -= 1
        else:
            iniCords[1] -= 1
        houses.add(tuple(iniCords))
    return houses

def calculateUniqueHousesWithRobo(file):
    initialPos = {(0, 0)}
    for paths in file:
        path,roboPath = paths[::2],paths[1::2]
        houses,roboHouses = uniqueHouses(path),uniqueHouses(roboPath)
        return len(houses.union(roboHouses).union(initialPos))

with open(inputPath,"r") as file:
    print(calculateUniqueHousesWithRobo(file))