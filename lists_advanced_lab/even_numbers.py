input_line = input().split(", ")
input_line = [int(i) for i in input_line]

list_with_index = []
for current_index in range(len(input_line)):
    if input_line[current_index] % 2 == 0:
        result = current_index
        list_with_index.append(result)
print(list_with_index)
