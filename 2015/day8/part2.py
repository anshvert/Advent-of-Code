"""
--- Part Two ---
Now, let's go the other way. In addition to finding the number of characters of code, you should now encode each code representation as a new string and find the number of characters of the
new encoded representation, including the surrounding double quotes.

For example:

"" encodes to "\"\"", an increase from 2 characters to 6.
"abc" encodes to "\"abc\"", an increase from 5 characters to 9.
"aaa\"aaa" encodes to "\"aaa\\\"aaa\"", an increase from 10 characters to 16.
"\x27" encodes to "\"\\x27\"", an increase from 6 characters to 11.
Your task is to find the total number of characters to represent the newly encoded strings minus the number of characters of code in each original string literal. For example, for the strings above,
the total encoded length (6 + 9 + 16 + 11 = 42) minus the characters in the original code representation (23, just like in the first part of this puzzle) is 42 - 23 = 19.
"""

filePath = "./input8.txt"

def calculateTotalCharacters(string):
    return len(string)

def calculateEncodedCharacters(string):
    count,it = 0,0
    while it < len(string):
        if string[it] == '"':
            count += 2
        elif string[it] == "\\":
            if string[it+1] == "x":
                count += 4
                it += 3
            else:
                count += 3
                it += 1
        else:
            pass
        count += 1
        it += 1
    return count

def encodedStrings(file):
    totalChars,totalEncodedChars = 0, 0
    for string in file:
        totalChars += calculateTotalCharacters(list(string.strip()))
        totalEncodedChars += calculateEncodedCharacters(list(string.strip()))
    return totalEncodedChars - totalChars

with open(filePath,"r") as file:
    print(encodedStrings(file))