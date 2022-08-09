single_string = input().split(", ")
beggars = int(input())
final_list = []
count_of_index = 0

sums_list_as_digits = []
for element in single_string:
    current_element = int(element)
    sums_list_as_digits.append(current_element)
while count_of_index < beggars:
    sum_of_current_beggar = 0
    for current_index in range(count_of_index, len(sums_list_as_digits), beggars):
        sum_of_current_beggar += sums_list_as_digits[current_index]
    count_of_index += 1
    final_list.append(sum_of_current_beggar)
print(final_list)