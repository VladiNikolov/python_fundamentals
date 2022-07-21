import re

pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
input_text = input()

searched_names = re.findall(pattern, input_text)
# print(*searched_names)
print(" ".join(searched_names))