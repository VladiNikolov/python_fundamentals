input_string = input()
strength = 0
new_text = ""

for element in range(len(input_string)):
    if strength > 0 and input_string[element] != ">":
        strength -= 1
    elif input_string[element] == ">":
        strength += int(input_string[element + 1])
        new_text += input_string[element]
    else:
        new_text += input_string[element]

print(new_text)