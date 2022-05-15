number_of_inputs = int(input())
sum_liters = 0
for i in range(number_of_inputs):
    current_input = int(input())
    sum_liters = sum_liters + current_input
    if sum_liters > 255:
        print("Insufficient capacity!")
        sum_liters = sum_liters - current_input
        continue

print(sum_liters)
