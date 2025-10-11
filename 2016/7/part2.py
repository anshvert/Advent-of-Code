def get_pal_trip(arr):
    trips = []
    for word in arr:
        i,j = 0,2
        while j < len(word):
            if word[i] == word[j]:
                trips.append(word[i:j+1])
            i += 1
            j += 1
    return trips

with open('input.txt', 'r') as input_file:
    puzzle_input = input_file.read().splitlines()
    valid_ips = 0
    for ip_string in puzzle_input:
        in_words,out_words,is_inside = [],[],False
        valid_in,valid_out = False,False
        current_word = ""

        for char in ip_string:
            if char == '[':
                out_words.append(current_word)
                current_word = ""
                is_inside = True
            elif char == ']':
                in_words.append(current_word)
                current_word = ""
                is_inside = False
            else:
                current_word += char

        out_words.append(current_word)
        out_words_triplets,in_words_triplets = set(get_pal_trip(out_words)), set(get_pal_trip(in_words))

        for word in out_words_triplets:
            if word[1] + word[0] + word[1] in in_words_triplets:
                valid_ips += 1
                break

    input_file.close()

print(valid_ips)