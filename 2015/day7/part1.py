"""
--- Day 7: Some Assembly Required ---
This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.

Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source,
but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.

The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.

For example:

123 -> x means that the signal 123 is provided to wire x.
x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.

For example, here is a simple circuit:

123 -> x
456 -> y
x AND y -> d
x OR y -> e
x LSHIFT 2 -> f
y RSHIFT 2 -> g
NOT x -> h
NOT y -> i
After it is run, these are the signals on the wires:

d: 72
e: 507
f: 492
g: 114
h: 65412
i: 65079
x: 123
y: 456
In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?

For Part2, Set the value of b in input file to the value received from a in part1 and Rerun the program !
"""
from collections import defaultdict

filePath = "./input7.txt"


def handleExtraction(dataMap,valueString):
    valueArr = valueString.split()
    if len(valueArr) == 1:
        if valueArr[0].isnumeric():
            return True,int(valueArr[0])
        else:
            if valueArr[0] in dataMap:
                return True, dataMap[valueArr[0]]
            return False, None
    else:
        if len(valueArr) == 2:
            if valueArr[1] in dataMap:
                return True,65535-dataMap[valueArr[1]]
            return False,None
        else:
            match valueArr[1]:
                case 'AND':
                    if valueArr[0].isnumeric() and valueArr[2].isnumeric():
                        return True,int(valueArr[0]) & int(valueArr[2])
                    elif valueArr[0].isnumeric():
                        if valueArr[2] in dataMap:
                            return True,dataMap[valueArr[2]] & int(valueArr[0])
                        return False,None
                    elif valueArr[2].isnumeric():
                        if valueArr[0] in dataMap:
                            return True,dataMap[valueArr[0]] & int(valueArr[2])
                        return False, None
                    else:
                        if valueArr[0] in dataMap and valueArr[2] in dataMap:
                            return True,dataMap[valueArr[0]] & dataMap[valueArr[2]]
                        return False, None
                case 'OR':
                    if valueArr[0].isnumeric() and valueArr[2].isnumeric():
                        return True, int(valueArr[0]) | int(valueArr[2])
                    elif valueArr[0].isnumeric():
                        if valueArr[2] in dataMap:
                            return True, dataMap[valueArr[2]] | int(valueArr[0])
                        return False, None
                    elif valueArr[2].isnumeric():
                        if valueArr[0] in dataMap:
                            return True, dataMap[valueArr[0]] | int(valueArr[2])
                        return False, None
                    else:
                        if valueArr[0] in dataMap and valueArr[2] in dataMap:
                            return True, dataMap[valueArr[0]] | dataMap[valueArr[2]]
                        return False, None
                case 'LSHIFT':
                    if valueArr[0].isnumeric() and valueArr[2].isnumeric():
                        return True, int(valueArr[0]) << int(valueArr[2])
                    elif valueArr[0].isnumeric():
                        if valueArr[2] in dataMap:
                            return True, dataMap[valueArr[2]] << int(valueArr[0])
                        return False, None
                    elif valueArr[2].isnumeric():
                        if valueArr[0] in dataMap:
                            return True, dataMap[valueArr[0]] << int(valueArr[2])
                        return False, None
                    else:
                        if valueArr[0] in dataMap and valueArr[2] in dataMap:
                            return True, dataMap[valueArr[0]] << dataMap[valueArr[2]]
                        return False, None
                case 'RSHIFT':
                    if valueArr[0].isnumeric() and valueArr[2].isnumeric():
                        return True, int(valueArr[0]) >> int(valueArr[2])
                    elif valueArr[0].isnumeric():
                        if valueArr[2] in dataMap:
                            return True, dataMap[valueArr[2]] >> int(valueArr[0])
                        return False, None
                    elif valueArr[2].isnumeric():
                        if valueArr[0] in dataMap:
                            return True, dataMap[valueArr[0]] >> int(valueArr[2])
                        return False, None
                    else:
                        if valueArr[0] in dataMap and valueArr[2] in dataMap:
                            return True, dataMap[valueArr[0]] >> dataMap[valueArr[2]]
                        return False, None


def getAssembly(file):
    currentWireData = defaultdict(int)
    while 'a' not in currentWireData:
        for instruction in file:
            value,key = instruction.split(' -> ')
            validValue,extractedValue = handleExtraction(currentWireData,value)
            key = key.strip()
            if validValue and key not in currentWireData:
                currentWireData[key] = extractedValue
        file.seek(0)
    return currentWireData['a']

with open(filePath,"r") as file:
    print(getAssembly(file))