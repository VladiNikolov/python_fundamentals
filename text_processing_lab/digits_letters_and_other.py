text = input()
digit = ""
letter = ""
other = ""

for ch in text:
    if ch.isdigit():
        digit += ch
    elif ch.isalpha():
        letter += ch
    else:
        other += ch
print(digit)
print(letter)
print(other)