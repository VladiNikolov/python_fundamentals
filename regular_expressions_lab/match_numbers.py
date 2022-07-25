import re

pattern = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d*)?($|(?=\s))"

input_string = input()

searched_pattern = re.finditer(pattern, input_string)

for match in searched_pattern:
    print(match.group(), end=" ")