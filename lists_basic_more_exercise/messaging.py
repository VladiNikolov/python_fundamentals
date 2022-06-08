sequence_of_numbers = input().split()
string = input()
result = 0
new_list = []
second_list = []
last_list = []
for element in sequence_of_numbers:
    sum_number = 0
    for number in element:
         sum_number += int(number)
    new_list.append(sum_number)
for index, el in enumerate(string):
    last_list.append(el)


for index in range(len(new_list)):
    if new_list[index] > len(last_list):
        result = new_list[index] // len(last_list)
    else:
        result = new_list[index]
    second_list.append(last_list[result])
    last_list.remove(last_list[result])

print("".join(second_list))





