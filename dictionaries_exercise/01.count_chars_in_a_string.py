input_line = input()
input_line = input_line.replace(" ", "")

words_dict = {}
for word in input_line:
    if word not in words_dict:
        words_dict[word] = 0
    words_dict[word] += 1
for keys, values in words_dict.items():
    print(f"{keys} -> {values}")

