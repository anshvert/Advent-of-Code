"""
--- Day 2: Bathroom Security ---
You arrive at Easter Bunny Headquarters under cover of darkness. However, you left in such a rush that you forgot to use the bathroom! Fancy office buildings like this one usually have keypad locks on their bathrooms, so you search the front desk for the code.

"In order to improve security," the document you find says, "bathroom codes will no longer be written down. Instead, please memorize and follow the procedure below to access the bathrooms."

The document goes on to explain that each button to be pressed can be found by starting on the previous button and moving to adjacent buttons on the keypad: U moves up, D moves down, L moves left, and R moves right. Each line of instructions corresponds to one button, starting at the previous button (or, for the first line, the "5" button); press whatever button you're on at the end of each line. If a move doesn't lead to a button, ignore it.

You can't hold it much longer, so you decide to figure out the code as you walk to the bathroom. You picture a keypad like this:

1 2 3
4 5 6
7 8 9
Suppose your instructions are:

ULL
RRDDD
LURDL
UUUUD
You start at "5" and move up (to "2"), left (to "1"), and left (you can't, and stay on "1"), so the first button is 1.
Starting from the previous button ("1"), you move right twice (to "3") and then down three times (stopping at "9" after two moves and ignoring the third), ending up with 9.
Continuing from "9", you move left, up, right, down, and left, ending with 8.
Finally, you move up four times (stopping at "2"), then down once, ending with 5.
So, in this example, the bathroom code is 1985.

Your puzzle input is the instructions from the document you found at the front desk. What is the bathroom code?
"""

digit_mapping = {
    '6U': '2',
    '7U': '3',
    '8U': '4',
    '3U': '1',
    'AU': '6',
    'BU': '7',
    'CU': '8',
    'DU': 'B',
    '2R': '3',
    '3R': '4',
    '5R': '6',
    '6R': '7',
    '7R': '8',
    '8R': '9',
    'AR': "B",
    'BR': "C",
    '3L': '2',
    '4L': '3',
    '6L': '5',
    '7L': '6',
    '8L': '7',
    '9L': '8',
    'BL': 'A',
    'CL': 'B',
    '1D': '3',
    '2D': '6',
    '3D': '7',
    '4D': '8',
    '6D': 'A',
    '7D': 'B',
    '8D': 'C',
    'BD': 'D'
}

with open("input.txt") as file:
    starting_pos = '5'
    codes = []
    for line in file.readlines():
        for char in line:
            digitKey = starting_pos + char
            if digitKey in digit_mapping:
                starting_pos = digit_mapping[digitKey]
        codes.append(starting_pos)
    print(codes)
