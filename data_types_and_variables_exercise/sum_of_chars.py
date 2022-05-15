number = int(input())

total_sum = 0
for i in range(number):
    current_char = input()
    char = ord(current_char)
    total_sum += char
print(f"The sum equals: {total_sum}")
