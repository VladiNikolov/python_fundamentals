import re

pattern = r"\b_([a-zA-Z0-9]+)\b"

input_line = input()
matches = re.findall(pattern, input_line)
print(",".join(matches))