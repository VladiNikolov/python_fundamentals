input_line = input().split()

my_dict = {}

for element in range(0, len(input_line), 2):
    key = input_line[element]
    value = input_line[element + 1]
    my_dict[key] = int(value)

print(my_dict)