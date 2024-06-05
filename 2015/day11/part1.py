"""
--- Day 11: Corporate Policy ---
Santa's previous password expired, and he needs help choosing a new one.

To help him remember his new password after the old one expires, Santa has devised a method of coming up with a password based on the previous one.
Corporate policy dictates that passwords must be exactly eight lowercase letters (for security reasons), so he finds his new password by incrementing his old password string repeatedly until it is valid.

Incrementing is just like counting with numbers: xx, xy, xz, ya, yb, and so on. Increase the rightmost letter one step; if it was z, it wraps around to a,
and repeat with the next letter to the left until one doesn't wrap around.

Unfortunately for Santa, a new Security-Elf recently started, and he has imposed some additional password requirements:

Passwords must include one increasing straight of at least three letters, like abc, bcd, cde, and so on, up to xyz. They cannot skip letters; abd doesn't count.
Passwords may not contain the letters i, o, or l, as these letters can be mistaken for other characters and are therefore confusing.
Passwords must contain at least two different, non-overlapping pairs of letters, like aa, bb, or zz.
For example:

hijklmmn meets the first requirement (because it contains the straight hij) but fails the second requirement (because it contains i and l).
abbceffg meets the third requirement (because it repeats bb and ff) but fails the first requirement.
abbcegjk fails the third requirement, because it only has one double letter (bb).
The next password after abcdefgh is abcdffaa.
The next password after ghijklmn is ghjaabcc, because you eventually skip all the passwords that start with ghi..., since i is not allowed.
Given Santa's current password (your puzzle input), what should his next password be?

Your puzzle input is cqjxjnds.
"""

puzzleInput = "cqjxxzaa"

def checkStraightLetters(string):
    i = 0
    while i < len(string) - 2:
        if ord(string[i + 2]) - ord(string[i + 1]) == 1 and ord(string[i + 1]) - ord(string[i]) == 1:
            return True
        i += 1
    return False

def forbiddenLetters(string):
    if "i" not in string and "o" not in string and "l" not in string:
        return True
    return False

def nonOverlappingPairs(string):
    c,i = 0,0
    while i < len(string)-1:
        if string[i] == string[i+1]:
            c += 1
            i += 2
        else:
            i += 1
    return c >= 2

def incrementString(string):
    lS,ind,incI = list(string),len(string)-1,None
    while ind >= 0:
        if string[ind] != "z":
            lS[ind] = chr(ord(string[ind]) + 1)
            break
        else:
            lS[ind] = 'a'
            ind -= 1
    return ''.join(lS)


def newPassword(string):
    tc,lc = 0,20
    while 1:
        if nonOverlappingPairs(string) and forbiddenLetters(string) and checkStraightLetters(string):
            print(string)
            break
        else:
            string = incrementString(string)
            if tc < lc:
                #print(string)
                tc += 1

newPassword(puzzleInput)


