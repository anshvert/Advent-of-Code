inputPath = "./input5.txt"

def vowelCheck(string):
    vowels = 0
    for char in string:
        if char in ['a','e','i','o','u']:
            vowels += 1
    return vowels >= 3

def consecutiveSameLetter(string):
    for i in range(1,len(string)):
        if string[i] == string[i-1]:
            return True

def disAllowed(string):
    disAllowedStrings = ["ab", "cd", "pq", "xy"]
    for strs in disAllowedStrings:
        if strs in string:
            return False
    return True

def niceStrings(file):
    count = 0
    for string in file:
        if vowelCheck(string) and consecutiveSameLetter(string) and disAllowed(string):
            count += 1
    return count

with open(inputPath,"r") as file:
    print(niceStrings(file))