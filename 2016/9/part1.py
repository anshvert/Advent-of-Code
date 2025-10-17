with open("input.txt") as f:
    line = f.read()
    f.close()

ind,copy_mode,copy_mode_num = 0,False,0
decompressed_string,current_string = "",""
current_multiplier = 1

while ind < len(line):
    if copy_mode:
        current_string += line[ind]
        copy_mode_num -= 1
        if not copy_mode_num:
            decompressed_string += current_string * current_multiplier
            copy_mode = False
            current_string = ""
        ind += 1
    else:
        if line[ind] == '(':
            copy_mode = True
            multiplier_string = ""
            while line[ind] != ')':
                multiplier_string += line[ind]
                ind += 1
            copy_mode_num, current_multiplier = map(int,multiplier_string[1:].split("x"))
        else:
            decompressed_string += line[ind]

        ind += 1

print(len(decompressed_string))