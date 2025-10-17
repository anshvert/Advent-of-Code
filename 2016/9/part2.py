with open("input.txt") as f:
    line = f.read().strip()

def calculate_decompressed_length(s):
    length = 0
    i = 0
    while i < len(s):
        if s[i] == '(':
            j = s.find(')', i)
            marker = s[i+1:j]
            chars, repeat = map(int, marker.split('x'))
            i = j + 1
            sub_string = s[i:i+chars]
            length += calculate_decompressed_length(sub_string) * repeat
            i += chars
        else:
            length += 1
            i += 1
    return length

print(calculate_decompressed_length(line))
