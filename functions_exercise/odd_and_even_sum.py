input_number = input()

even_sum = 0
odd_sum = 0
list_integer = []
for current_number in range(len(input_number)):
    list_integer.append(int(input_number[current_number]))

for number in list_integer:
    if number % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")
