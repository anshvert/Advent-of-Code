def sol1():
    with open("input.txt") as f:
        lines = f.readlines()
        currentReading,zeroCount = 50,0
        for line in lines:
            direction,rotation = line[0],int(line[1:])
            rotation %= 100
            if direction == "L":
                if rotation <= currentReading:
                    currentReading -= rotation
                else:
                    currentReading += (100 - rotation)
            else:
                if rotation + currentReading < 100:
                    currentReading += rotation
                else:
                    currentReading -= (100 - rotation)
            if currentReading == 0:
                zeroCount += 1
        print("Password 1",zeroCount)

def sol2():
    with open("input.txt") as f:
        lines = f.readlines()
        currentReading,prevReading,zeroCount = 50,None,0
        for line in lines:
            direction,rotation = line[0],int(line[1:])
            zeroCount += rotation // 100
            rotation %= 100
            prevReading = currentReading
            if direction == "L":
                if rotation <= currentReading:
                    currentReading -= rotation
                else:
                    currentReading += (100 - rotation)
            else:
                if rotation + currentReading < 100:
                    currentReading += rotation
                else:
                    currentReading -= (100 - rotation)
            if currentReading == 0:
                zeroCount += 1
            elif prevReading != 0 and (prevReading > currentReading and direction == "R" or prevReading < currentReading and direction == "L"):
                zeroCount += 1
        print("Password 2",zeroCount)

sol1()
sol2()
