file_path = "inputs/input1.txt"



def maxCalories(file):
    maxCal = 0
    cCal = 0
    allCals = []
    for line in file:
        # print(type(line),len(line))
        if len(line) != 1:
            cCal += int(line[:-1]) if line[-1] == "\n" else int(line)
        else:
            maxCal = max(maxCal, cCal)
            allCals.append(cCal)
            cCal = 0
    allCals.append(cCal)
    return maxCal,allCals

def top3Cal(file):

    _,allCals = maxCalories(file)
    allCals.sort(reverse=True)
    return sum(allCals[:3])

with open(file_path,"r") as file:
    print(top3Cal(file))

