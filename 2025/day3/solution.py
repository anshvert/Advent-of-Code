import sys

def sol1():
    with open("input.txt") as f:
        lines = f.readlines()
        totalJoltage = 0
        for line in lines:
            maxJoltage = -sys.maxsize
            for i in range(len(line)):
                for j in range(i+1,len(line)):
                    maxJoltage = max(maxJoltage,int(line[i] + line[j]))
            totalJoltage += maxJoltage

        print("Max Joltage is:",totalJoltage)

def sol2():
    with open("input.txt") as f:
        lines = f.readlines()
        totalJoltage = 0
        for line in lines:
            canDiscard,batteryStack = len(line.strip()) - 12,[]
            for char in line.strip():
                if not batteryStack:
                    batteryStack.append(char)
                else:
                    if not canDiscard:
                        batteryStack.append(char)
                    else:
                        while batteryStack and char > batteryStack[-1] and canDiscard:
                            batteryStack.pop()
                            canDiscard -= 1
                        batteryStack.append(char)
            totalJoltage += int(''.join(batteryStack[:12]))
        print("Max Joltage is:",totalJoltage)

sol1()
sol2()