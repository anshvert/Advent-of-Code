
def red_nose_reverse(puzzle_input):
    replacements = []
    molecule = ""
    for line in puzzle_input:
        if "=>" in line:
            src, dest = line.strip().split(" => ")
            replacements.append((dest, src))
        elif line.strip():
            molecule = line.strip()

    replacements.sort(key=lambda x: len(x[0]), reverse=True)

    steps = 0
    while molecule != "e":
        for dest, src in replacements:
            if dest in molecule:
                molecule = molecule.replace(dest, src, 1)
                steps += 1
                break

    return steps

with open("./input.txt", "r") as puzzle_input:
    print(red_nose_reverse(puzzle_input))
