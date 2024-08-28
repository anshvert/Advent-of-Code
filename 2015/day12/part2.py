"""
--- Part Two ---
Uh oh - the Accounting-Elves have realized that they double-counted everything red.

Ignore any object (and all of its children) which has any property with the value "red". Do this only for objects ({...}), not arrays ([...]).

[1,2,3] still has a sum of 6.
[1,{"c":"red","b":2},3] now has a sum of 4, because the middle object is ignored.
{"d":"red","e":[1,2,3,4],"f":5} now has a sum of 0, because the entire structure is ignored.
[1,"red",5] has a sum of 6, because "red" in an array has no effect.

"""

import json

filePath = "./input12.txt"

def is_number(val):
    return isinstance(val,(int, float, complex))

def is_array(val):
    return isinstance(val, list)

def is_dict(val):
    return isinstance(val, dict)

def validDict(dikt):
    return "red" not in dikt.values()

def JSAbacusFramework(file):
    def countNumbers(data):
        nonlocal count
        if is_dict(data):
            if not validDict(data): return
            for key, val in data.items():
                if is_number(val):
                    count += val
                else:
                    countNumbers(val)
        elif is_array(data):
            for val in data:
                if is_number(val):
                    count += val
                else:
                    countNumbers(val)

    count = 0
    content = file.read()
    parsedData = json.loads(content)
    countNumbers(parsedData)
    return count

with open(filePath,"r") as file:
    print(JSAbacusFramework(file))
