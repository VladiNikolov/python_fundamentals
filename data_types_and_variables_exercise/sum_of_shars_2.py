number = int(input())

sum = 0
i = 0
while i < number:
    current_input = input()
    result = ord(current_input)
    sum = sum + result
    i += 1
print(f"The sum equals: {sum}")