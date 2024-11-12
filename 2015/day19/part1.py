"""
The North Pole is equipped with a Red-Nosed Reindeer nuclear fusion/fission plant, capable of constructing any Red-Nosed Reindeer molecule you need. It works by starting with some input molecule and then doing a series of replacements, one per step, until it has the right molecule.

However, the machine has to be calibrated before it can be used. Calibration involves determining the number of molecules that can be generated in one step from a given starting point.

For example, imagine a simpler machine that supports only the following replacements:

H => HO
H => OH
O => HH

Given the replacements above and starting with HOH, the following molecules could be generated:

    HOOH (via H => HO on the first H).
    HOHO (via H => HO on the second H).
    OHOH (via H => OH on the first H).
    HOOH (via H => OH on the second H).
    HHHH (via O => HH).

So, in the example above, there are 4 distinct molecules (not five, because HOOH appears twice) after one replacement from HOH. Santa's favorite molecule, HOHOHO, can become 7 distinct molecules (over nine replacements: six from H, and three from O).

The machine replaces without regard for the surrounding characters. For example, given the string H2O, the transition H => OO would result in OO2O.

Your puzzle input describes all of the possible replacements and, at the bottom, the medicine molecule for which you need to calibrate the machine. How many distinct molecules can be created after all the different ways you can do one replacement on the medicine molecule?
"""

from collections import defaultdict

def uniqueStrings(molMap,string):
    unique = set()
    for ind,val in enumerate(string):
        if val in molMap.keys():
            for xx in molMap[val]:
                uniqueStr = string[:ind] + xx + string[ind+1:]
                unique.add(uniqueStr)

    print(len(unique))

    i = 1
    while i < len(string):
        cs = string[i-1:i+1]
        if cs in molMap.keys():
            for xx in molMap[cs]:
                uniqueStr = string[:i-1] + xx + string[i+1:]
                unique.add(uniqueStr)
        i += 1

    return len(unique)

def redNose(puzzleInput):
    perms = defaultdict(list)
    string = ""
    for line in puzzleInput:
        try:
            key,val = line.split("=>")
            perms[key.strip()].append(val.strip())
        except ValueError:
            string = line

    return uniqueStrings(perms,string)

with open("input.txt", "r") as puzzle_input:
    print(redNose(puzzle_input))