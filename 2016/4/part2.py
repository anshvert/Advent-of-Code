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

--- Part Two ---
With all the decoy data out of the way, it's time to decrypt this list and get moving.

The room names are encrypted by a state-of-the-art shift cipher, which is nearly unbreakable without the right software.
However, the information kiosk designers at Easter Bunny HQ were not expecting to deal with a master cryptographer like yourself.

To decrypt a room name, rotate each letter forward through the alphabet a number of times equal to the room's sector ID.
A becomes B, B becomes C, Z becomes A, and so on. Dashes become spaces.

For example, the real name for qzmt-zixmtkozy-ivhz-343 is very encrypted name.

What is the sector ID of the room where North Pole objects are stored?
"""

from collections import Counter

total_sector_sum = 0
real_rooms = []

with open("input.txt") as file:
    lines = file.read().splitlines()
    for room in lines:
        room_components = room.split("-")
        word_string = "".join(room_components[:-1])
        sector_id, checksum = room_components[-1].split("[")
        checksum = checksum[:-1]

        counts = Counter(word_string)
        sorted_letters = sorted(counts.keys(), key=lambda letter: (-counts[letter], letter))
        generated_checksum = "".join(sorted_letters[:5])

        if generated_checksum == checksum:
            total_sector_sum += int(sector_id)
            real_rooms.append([room_components, int(sector_id)])

    file.close()

print("Total Sector Sum ",total_sector_sum)

for room_component, sector_id in real_rooms:
    decrypted_parts = []
    for encrypted_part in room_component[:-1]:
        decrypted_word = "".join([
            chr(((ord(letter) - ord('a') + sector_id) % 26) + ord('a'))
            for letter in encrypted_part
        ])
        decrypted_parts.append(decrypted_word)
    
    decrypted_name = " ".join(decrypted_parts)

    if "north" in decrypted_name:
        print(f"Found target room: '{decrypted_name}' with Sector ID: {sector_id}")