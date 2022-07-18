input_string = input()

encrypted_version_list = []
for character in input_string:
    current_character = ord(character) + 3
    encrypted_version_list.append(chr(current_character))
print("".join(encrypted_version_list))
