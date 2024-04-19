# """
# --- Day 8: Matchsticks ---
# Space on the sleigh is limited this year, and so Santa will be bringing his list as a digital copy. He needs to know how much space it will take up when stored.
#
# It is common in many programming languages to provide a way to escape special characters in strings. For example, C, JavaScript, Perl, Python, and even PHP handle special characters in very similar ways.
#
# However, it is important to realize the difference between the number of characters in the code representation of the string literal and the number of characters in the in-memory string itself.
#
# For example:
#
# "" is 2 characters of code (the two double quotes), but the string contains zero characters.
# "abc" is 5 characters of code, but 3 characters in the string data.
# "aaa\"aaa" is 10 characters of code, but the string itself contains six "a" characters and a single, escaped quote character, for a total of 7 characters in the string data.
# "\x27" is 6 characters of code, but the string itself contains just one - an apostrophe ('), escaped using hexadecimal notation.
# Santa's list is a file that contains many double-quoted string literals, one on each line. The only escape sequences used are \\ (which represents a single backslash), \" (which represents a lone double-quote character), and \x plus two hexadecimal characters (which represents a single character with that ASCII code).
#
# Disregarding the whitespace in the file, what is the number of characters of code for string literals minus the number of characters in memory for the values of the strings in total for the entire file?
#
# For example, given the four strings above, the total number of characters of string code (2 + 5 + 10 + 6 = 23) minus the total number of characters in memory for string values (0 + 3 + 7 + 1 = 11) is 23 - 11 = 12.
# """

filePath = "./input8.txt"

def calculateTotalCharacters(string):
    return len(string)

def calculateInMemoryCharacters(string):
    count,it = 0,0
    while it < len(string):
        if string[it] == "\\":
            count += 1
            if string[it+1] == "x":
                it += 4
            else:
                it += 2
        else:
            count += 1
            it += 1
    return count - 2

def matchSticks(file):
    totalChars,totalInMemoryChars = 0,0
    for string in file:
        totalChars += calculateTotalCharacters(list(string.strip()))
        totalInMemoryChars += calculateInMemoryCharacters(list(string.strip()))
    return totalChars - totalInMemoryChars

with open(filePath,"r") as file:
    print(matchSticks(file))