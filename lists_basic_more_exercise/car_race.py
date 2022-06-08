sequence_of_numbers = input().split()

sequence_of_numbers = [int(i) for i in sequence_of_numbers]

middle_string =  len(sequence_of_numbers) // 2
left_racer = sequence_of_numbers[0:middle_string]
right_racer = sequence_of_numbers[middle_string + 1::]

sum_left_index = 0
sum_right_index = 0
for index_in_first_race in range(len(left_racer)):
    if left_racer[index_in_first_race] == 0:
        sum_left_index = sum_left_index * 0.80
    else:
        sum_left_index += left_racer[index_in_first_race]
right_racer.reverse()
for index_in_second_race in range(len(right_racer)):
    if right_racer[index_in_second_race] == 0:
        sum_right_index = sum_right_index * 0.80
    else:
        sum_right_index += right_racer[index_in_second_race]

if sum_left_index < sum_right_index:
    winner = "left"
    sum = sum_left_index
else:
    winner = "right"
    sum = sum_right_index
print(f"The winner is {winner} with total time: {sum:.1f}")

