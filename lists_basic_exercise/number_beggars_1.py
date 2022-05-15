input_line = input().split(", ")
beggars = int(input())
beggar_list = []
count_of_index = 0
temp_sum = 0
sums_list_as_digits = [] #input_line = [int(i) for i in input_line] ->list comprehension

for index in range(len(input_line)):
    sums_list_as_digits.append(int(input_line[index]))

while count_of_index < beggars:
    for element in range(count_of_index, len(sums_list_as_digits), beggars):
        temp_sum += sums_list_as_digits[element]
    beggar_list.append(temp_sum)
    temp_sum = 0
    count_of_index += 1

print(beggar_list)

