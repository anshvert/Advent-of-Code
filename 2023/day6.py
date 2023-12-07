filePath = "inputs/day6.txt"


def findAWay(time, dist):
    cWays = 0
    for t in range(1, time + 1):
        if t * (time - t) > dist:
            cWays += 1
    return cWays


def findWays(rTimes, rDist):
    ans = 1
    for i in range(len(rTimes)):
        time, dist = rTimes[i], rDist[i]
        ans *= findAWay(time, dist)
    return ans


def ways2Win(inputFile):
    raceInput, raceMap = [], dict()
    for race in inputFile:
        raceInput.append(race.rstrip("\n").split(" "))
    raceTimes, raceDistances = [], []
    raceTimeString, raceDistString = "", ""
    # print(raceInput)
    for tym in raceInput[0]:
        if tym.isdigit():
            raceTimes.append(int(tym))
            raceTimeString += tym
    for dis in raceInput[1]:
        if dis.isdigit():
            raceDistances.append(int(dis))
            raceDistString += dis
    # print(raceTimes,raceDistances)
    # P1
    # return findWays(raceTimes,raceDistances)
    # P2 46561107
    return findAWay(int(raceTimeString), int(raceDistString))


with open(filePath, "r") as file:
    print(ways2Win(file))
    file.close()
