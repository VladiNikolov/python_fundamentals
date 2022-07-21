import re

pattern = r"\+359( |-)2\1\d{3}\1\d{4}\b"
input_number = input()

searched_pattern = [numbers.group() for numbers in re.finditer(pattern, input_number)]
print(", ".join(searched_pattern))
