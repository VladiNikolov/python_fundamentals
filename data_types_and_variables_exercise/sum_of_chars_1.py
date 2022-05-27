input_number = int(input())

total_sum = 0
for _ in range(input_number):
    current_input = input()
    result = ord(current_input)
    total_sum += result
print(f"The sum equals: {total_sum}")