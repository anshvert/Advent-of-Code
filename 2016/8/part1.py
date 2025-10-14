screen = [[0 for x in range(50)] for y in range(6)]

def rotate_row_by(mat,row,freq):
    new_row = mat[row][:]
    for i in range(len(mat[row])):
        new_row[i] = mat[row][(i - freq) % len(mat[row])]
    mat[row] = new_row

def rotate_column_by(mat,col,freq):
    new_col = [mat[i][col] for i in range(len(mat))]
    for i in range(len(mat)):
        new_col[i] = mat[(i - freq) % len(mat)][col]
    for j in range(len(mat)):
        mat[j][col] = new_col[j]

with open("input.txt") as f:
    instructions = f.read().splitlines()
    f.close()

for instruction in instructions:
    instruction_parts = instruction.split(" ")
    if instruction_parts[0] == "rect":
        rect_y,rect_x = map(int,instruction_parts[1].split("x"))
        for i in range(rect_x):
            for j in range(rect_y):
                screen[i][j] = screen[i][j] = 1
    elif instruction_parts[0] == "rotate":
        if instruction_parts[1] == 'row':
            row,freq = int(instruction_parts[2].split("=")[1]), int(instruction_parts[4])
            rotate_row_by(screen,row,freq)
        elif instruction_parts[1] == 'column':
            col,freq = int(instruction_parts[2].split("=")[1]), int(instruction_parts[4])
            rotate_column_by(screen,col,freq)

lit = 0

for i in range(len(screen)):
    for j in range(len(screen[i])):
        if screen[i][j] == 1: lit += 1

for row in screen:
    print(row)
print("Lit", lit)

# Part2 had me a fking headache