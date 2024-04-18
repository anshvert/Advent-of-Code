from collections import defaultdict

inputPath = "./input5.txt"

"""
Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.

Now, a nice string is one with all of the following properties:

It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
"""

def twoPairs(string):
    stringMap = defaultdict(set)
    for i in range(1,len(string)):
        stringMap[string[i-1]+string[i]].update({i, i - 1})
    for Set in stringMap.values():
        if len(Set) >= 4:
            return True
    return False

def letterRepeat(string):
    for i in range(1,len(string)-1):
        if string[i-1] == string[i+1]:
            return True
    return False

def niceStrings(file):
    count = 0
    for string in file:
        if twoPairs(string) and letterRepeat(string):
            count += 1
    return count


with open(inputPath,"r") as file:
    print(niceStrings(file))