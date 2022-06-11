input_number = input().split()

new_list_with_intehers = []
for number in input_number:
    current_number = int(number)
    new_list_with_intehers.append(current_number)
print(sorted(new_list_with_intehers))