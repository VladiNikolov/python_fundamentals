def is_even(number):
    if int(number) % 2 == 0:
        return True
    return False


numbers = input().split()
filtered_numbers = []
for current_number in numbers:
    if is_even(current_number):
        filtered_numbers.append(int(current_number))
print(filtered_numbers)