input_line = input()

words_dict = {}
for letter in input_line:
    if letter == " ":
        continue
    else:
        if letter not in words_dict:
            words_dict[letter] = 1
        else:
            words_dict[letter] += 1
for element in words_dict:
    print(f"{element} -> {words_dict[element]}")
