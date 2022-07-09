letters_dict = {}

input_symbol = "".join(i for i in input().split())
for letter in input_symbol:
    if letter not in letters_dict:
        letters_dict[letter] = 0
    letters_dict[letter] += 1

for key in letters_dict.keys():
    print(f"{key} -> {letters_dict[key]}")