input_text = input()
my_list = []
for element in range(len(input_text)):
    if input_text[element] == ":":
        my_list.append(input_text[element] + input_text[element + 1])
for i in my_list:
    print("".join(i))

