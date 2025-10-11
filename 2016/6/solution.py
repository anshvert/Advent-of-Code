from collections import defaultdict

column_data = defaultdict(dict)
message = ""

with open("input.txt") as input_file:
    lines = input_file.read().splitlines()
    for word in lines:
        for ind,char in enumerate(word):
            column_data[ind][char] = column_data[ind].get(char, 0) + 1

    for key,value in column_data.items():
        max_key, max_value = min(value.items(), key=lambda x: x[1]) # max for part1 :)
        message += max_key

    input_file.close()

print(message)