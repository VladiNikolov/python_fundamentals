input_electrons = int(input())
number_of_electrons = input_electrons

sum = 0
number = 1
filled_shells = []
while sum < input_electrons:
    current_number = 2 * number**2
    sum += current_number
    if sum <= input_electrons:

        filled_shells.append(current_number)
        number += 1
    else:
        sum -= current_number
        filled_shells.append(input_electrons - sum)
        break

print(filled_shells)