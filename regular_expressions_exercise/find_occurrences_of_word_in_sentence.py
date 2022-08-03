import re
input_string = input()
searched_word = input()

pattern = fr"\b{searched_word}\b"

matches = re.findall(pattern, input_string, re.IGNORECASE)
print(len(matches))