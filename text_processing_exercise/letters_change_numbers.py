input_string = [i for i in input().split()]
result = 0

for element in input_string:
    first_char = element[0]
    last_char = element[-1]
    digits = int(element[1:-1])
    if first_char.isupper():
        result += (digits / (ord(first_char) - 64))
    if first_char.islower():
        result += digits * (ord(first_char) - 96)
    if last_char.isupper():
        result -= (ord(last_char) - 64)
    if last_char.islower():
        result += (ord(last_char) - 96)

print(f"{result:.2f}")
