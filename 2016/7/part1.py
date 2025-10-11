def has_palindrome(word):
    if len(word) < 4: return False
    i,j = 0,4
    while j <= len(word):
        if word[i:j] == word[i:j][::-1] and word[i] != word[i+1]:
            return True
        i += 1
        j += 1
    return False

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

        for word in in_words:
            if has_palindrome(word):
                valid_in = True
                break
        for word in out_words:
            if has_palindrome(word):
                valid_out = True
                break

        if not valid_in and valid_out:
            print(ip_string)
            valid_ips += 1

    input_file.close()

print(valid_ips)