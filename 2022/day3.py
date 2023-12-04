filePath = "inputs/input3.txt"

def priorityScore(file):
    totalSum = 0
    for comp in file:
        compartment = comp.rstrip("\n")
        comp1,comp2 = compartment[:len(compartment) // 2],compartment[len(compartment) // 2:]
        #print(comp1,comp2)
        commonString = set(comp1).intersection(set(comp2))
        #print(commonString)
        for i in commonString:
            if i.isupper():
                totalSum += ord(i) - 38
            else:
                totalSum += ord(i) - 96
    return totalSum

def badgeScore(file):
    totalSum,curElv,curElvB = 0,0,[]
    for comp in file:
        if curElv < 3:
            curElvB.append(set(comp.rstrip("\n")))
            curElv += 1
            if curElv == 3:
                commonB = curElvB[0].intersection(curElvB[1]).intersection(curElvB[2])
                for i in commonB:
                    if i.isupper():
                        totalSum += ord(i) - 38
                    else:
                        totalSum += ord(i) - 96
                #print(commonB)
                curElv,curElvB = 0,[]

    return totalSum

with open(filePath,"r") as file:
    print(badgeScore(file))