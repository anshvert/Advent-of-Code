inputFilePath = "inputs/day1.txt"
ans = 0

def calibrationValue1(st):
    digits = []
    for i in st:
        if i.isdigit():
            digits.append(i)
    return int(digits[0] + digits[-1])

def getNumberIndexes(st):
    digitIndexes = []
    for ind,val in enumerate(st):
        if val.isdigit():
            digitIndexes.append((val,ind))
    return digitIndexes
def calibrationValue2(st):
    numLetters = ["one","two","three","four","five","six","seven","eight","nine"]
    letterIndexes = []
    # Order
    for ind,val in enumerate(numLetters):
        if val in st:
            letterIndexes.append((str(ind+1),st.index(val)))
    # Reverse Order
    for ind,val in enumerate(numLetters):
        if val[::-1] in st[::-1]:
            letterIndexes.append((str(ind+1),len(st) - st[::-1].index(val[::-1])))
    normalDigitIndexes = getNumberIndexes(st)
    #print(st,letterIndexes)
    #print(normalDigitIndexes)
    allIndexes = sorted(letterIndexes+normalDigitIndexes,key=lambda x: x[1])
    #print(allIndexes)
    return int(allIndexes[0][0] + allIndexes[-1][0])

with open(inputFilePath, "r") as file:
    for line in file:
        ans += calibrationValue2(line)

print(ans)
