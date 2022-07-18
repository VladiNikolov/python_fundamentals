input_string = input()
new_string = ""
character = ""

for char in input_string:
    if char != character:
        new_string += char
        character = char
print(new_string)