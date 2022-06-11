input_numbers = input().split()

for current_number in range(len(input_numbers)):
    input_numbers[current_number] = int(input_numbers[current_number])
print(sorted(input_numbers))