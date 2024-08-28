"""
--- Day 12: JSAbacusFramework.io ---
Santa's Accounting-Elves need help balancing the books after a recent order. Unfortunately, their accounting software uses a peculiar storage format. That's where you come in.

They have a JSON document which contains a variety of things: arrays ([1,2,3]), objects ({"a":1, "b":2}), numbers, and strings. Your first job is to simply find all of the numbers throughout the document and add them together.

For example:

[1,2,3] and {"a":2,"b":4} both have a sum of 6.
[[[3]]] and {"a":{"b":4},"c":-1} both have a sum of 3.
{"a":[-1,1]} and [-1,{"a":1}] both have a sum of 0.
[] and {} both have a sum of 0.
You will not encounter any strings containing numbers.

What is the sum of all numbers in the document?
"""

import json

filePath = "./input12.txt"

def is_number(val):
    return isinstance(val,(int, float, complex))

def is_array(val):
    return isinstance(val, list)

def is_dict(val):
    return isinstance(val, dict)

def JSAbacusFramework(file):
    def countNumbers(data):
        nonlocal count
        if is_dict(data):
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

