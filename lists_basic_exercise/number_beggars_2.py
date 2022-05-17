input_str = input().split(", ")
number_beggars = int(input())

sum = 0
beggar_list = []
beggar_list_int = []

for index in range(len(input_str)):
    beggar_list_int.append(int(input_str[index]))

for number in range(number_beggars):
    for element in range(number, len(beggar_list_int), number_beggars):
        sum = sum + beggar_list_int[element]
    beggar_list.append(sum)
    sum = 0

print(beggar_list)