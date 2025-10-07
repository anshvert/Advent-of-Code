"""
--- Day 4: Security Through Obscurity ---
Finally, you come across an information kiosk with a list of rooms. Of course, the list is encrypted and full of decoy data,
but the instructions to decode the list are barely hidden nearby. Better remove the decoy data first.

Each room consists of an encrypted name (lowercase letters separated by dashes) followed by a dash, a sector ID, and a checksum in square brackets.

A room is real (not a decoy) if the checksum is the five most common letters in the encrypted name, in order, with ties broken by alphabetization.
For example:

aaaaa-bbb-z-y-x-123[abxyz] is a real room because the most common letters are a (5), b (3), and then a tie between x, y, and z,
which are listed alphabetically.
a-b-c-d-e-f-g-h-987[abcde] is a real room because although the letters are all tied (1 of each), the first five are listed alphabetically.
not-a-real-room-404[oarel] is a real room.
totally-real-room-200[decoy] is not.
Of the real rooms from the list above, the sum of their sector IDs is 1514.

What is the sum of the sector IDs of the real rooms?
"""

with open("input.txt") as file:
    lines = file.read().splitlines()
    for room in lines:
        room_components = room.split("-")
        word_string = "".join(room_components[:-1])
        print(word_string)
        sector_id, checksum = room_components[-1].split("[")
        checksum = checksum[:-1]
        print(sector_id, checksum)
        word_string_sorted = sorted(word_string,key=lambda x: [word_string.count(x), x])
        # for word in checksum:
        # later biach

