def get_characters(first_character, second_character ):
    collected_characters = []
    for current_character in range(ord(first_character) + 1, ord(second_character)):
        collected_characters.append(chr(current_character))
    return collected_characters

first_character = input()
second_character = input()
result = (get_characters(first_character, second_character))
print(" ".join(result))