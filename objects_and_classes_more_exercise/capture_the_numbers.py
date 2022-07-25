import re

line = input()
pattern = r"\d+"

while True:
    if line:
        match = re.findall(pattern, line)
        if match:
            print(" ".join(match), end = " ")
    else:
        break

    line = input()
