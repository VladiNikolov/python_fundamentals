input_line = input().split()
input_line = [int(i) for i in input_line]

my_list = []
for element in range(len(input_line)):
    if input_line[element] > 0:
        my_list.append(input_line[element] * -1)
    else:
        my_list.append(input_line[element] * -1)
print(my_list)