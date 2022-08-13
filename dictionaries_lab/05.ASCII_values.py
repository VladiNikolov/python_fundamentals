characters = input().split(", ")

char_dict = {}
for char in characters:
    if char not in char_dict:
        char_dict[char] = ord(char)
print(char_dict)
