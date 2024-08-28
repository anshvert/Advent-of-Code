"""
--- Part Two ---
Seeing how reindeer move in bursts, Santa decides he's not pleased with the old scoring system.
Instead, at the end of each second, he awards one point to the reindeer currently in the lead.
(If there are multiple reindeer tied for the lead, they each get one point.) He keeps the traditional 2503 second time limit,
of course, as doing otherwise would be entirely ridiculous.

Given the example reindeer from above, after the first second, Dancer is in the lead and gets one point.
He stays in the lead until several seconds into Comet's second burst: after the 140th second, Comet pulls into the lead and gets his first point.
Of course, since Dancer had been in the lead for the 139 seconds before that, he has accumulated 139 points by the 140th second.

After the 1000th second, Dancer has accumulated 689 points, while poor Comet, our old champion, only has 312. So, with the new scoring system,
Dancer would win (if the race ended at 1000 seconds).

Again given the descriptions of each reindeer (in your puzzle input), after exactly 2503 seconds, how many points does the winning reindeer have?
"""

import copy

def ReindeerOlympics(fileData):

    statDict = dict()

    for stat in fileData:
        statSplit = stat.split()
        name,speed,time,rest = statSplit[0],int(statSplit[3]),int(statSplit[6]),int(statSplit[-2])
        statDict[name] = [speed,time,rest,0,0]

    for sec in range(1,quesTime + 1):
        maxD = 0
        for key,val in statDict.items():
            orgSec = copy.deepcopy(sec)
            orgSec %= (val[1] + val[2])
            if 1 <= orgSec <= val[1]:
                val[3] += val[0]
            maxD = max(maxD, val[3])
        for key,val in statDict.items():
            if val[3] == maxD:
                val[4] += 1
    return max([i[4] for i in statDict.values()])

filePath = "./input14.txt"
quesTime = 2503

with open(filePath, "r") as file:
    print(ReindeerOlympics(file))