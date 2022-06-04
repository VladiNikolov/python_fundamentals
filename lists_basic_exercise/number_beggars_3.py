input_strings = input().split(", ")
beggars = int(input())

sum_list = []
beggar_list = []
temp_sum = 0
count_index = 0

for i in range(len(input_strings)):
    sum_list.append(int(input_strings[i]))

while count_index < beggars:
    for element in range(count_index, len(sum_list), beggars):
        temp_sum += sum_list[element]
    beggar_list.append(temp_sum)
    temp_sum = 0
    count_index += 1
print(beggar_list)



